# ID da página está no id das classes: class="event__match event__match--static event__match--last event__match--twoLine"
# <a class="event__more event__more--static" href="#">Mostrar mais jogos</a> <== Botão para mostrar mais jogos
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

def letras_maiusculas(string):
  letras = ''
  for i in range(len(string)):
    if string[i].isupper():
      letras = letras + string[i]
  return letras

# tempo = FT - Full time (Os 2 tempos), 1T
# se o campeonato for europeu, a temporada é divida entre dois anos, por exemplo Premier league 2023-2024
def get_data_from_tournament(nomeDataset, pais, campeonato, tempos):

  driver = webdriver.Chrome()
  driver.get(f"https://www.flashscore.com.br/futebol/{pais}/{campeonato}/resultados/")
  WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler'))).click()
  fields = driver.find_elements(By.CLASS_NAME, "event__round.event__round--static")
  for i, field in enumerate(fields):
    try:
      btn_more = driver.find_element(By.CLASS_NAME, 'event__more')
      WebDriverWait(driver, 20).until(EC.element_to_be_clickable(btn_more)).click()
      fields = driver.find_elements(By.CLASS_NAME, "event__round.event__round--static")
    except:
      pass
  # event__participant event__participant--away Tag Away team
  fields = driver.find_elements(By.CLASS_NAME, "event__match.event__match--static.event__match--twoLine")
  id_partidas = []
  for i, field in enumerate(fields):
    id_partidas.append(field.get_attribute('id').split('_')[2])
  driver.get(f'https://www.flashscore.com.br/jogo/f96Ipi6G/#/resumo-de-jogo/estatisticas-de-jogo/1')
  estatisticas = driver.find_elements(By.CLASS_NAME, '_row_1csk6_9')
  colunasEstatisticas = ['Data', 'Round', 'HomeTeam', 'AwayTeam']
  colunasDataSet = ['Data', 'Round', 'HomeTeam', 'AwayTeam', 'HT0G', 'AT0G', 'HT1G', 'AT1G', 'HT2G', 'AT2G']
  linhas = []
  for tempo in tempos:
    for i, field in enumerate(estatisticas):
      colunasDataSet.append(letras_maiusculas(field.text.split('\n')[1].replace('xG',''))+f"HT{tempo}T")
      colunasDataSet.append(letras_maiusculas(field.text.split('\n')[1].replace('xG',''))+f"AT{tempo}T")
  for i, field in enumerate(estatisticas):
    colunasEstatisticas.append(field.text.split('\n')[1])
  
  for j, id_partida in enumerate(id_partidas):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'duelParticipant__home')))
    driver.get(f'https://www.flashscore.com.br/jogo/{id_partida}/#/resumo-de-jogo/resumo-de-jogo')
    first_time = True
    partidaLinha = []
    ht1g = ''
    at1g = ''
    ht2g = ''
    at2g = ''
    # smv__incidentsHeader section__title
    gols_tempos = driver.find_elements(By.CLASS_NAME, 'smv__incidentsHeader')
    for i, field in enumerate(gols_tempos):
      gols = field.text.split("\n")[1]
      if (field.text.split("\n")[0] == "1º TEMPO"):
        ht1g = gols.split('-')[0].replace(' ', '')
        at1g = gols.split('-')[1].replace(' ', '')
      elif (field.text.split("\n")[0] == "2º TEMPO"):
        ht2g = gols.split('-')[0].replace(' ', '')
        at2g = gols.split('-')[1].replace(' ', '')
    for tempo in tempos:
      WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'duelParticipant__home')))
      driver.get(f'https://www.flashscore.com.br/jogo/{id_partida}/#/resumo-de-jogo/estatisticas-de-jogo/{tempo}')
      # Pegar Posse de bola 1° tempo - _value_1c6mj_5 _homeValue_1c6mj_10 
      # [[partida 1], [partida 2], [partida 3]...]
      # Rodada = tournamentHeader__country (a com href)
      # Data do jogo - duelParticipant__startTime
      homeTeam = driver.find_element(By.CLASS_NAME, 'duelParticipant__home').text
      awayTeam = driver.find_element(By.CLASS_NAME, 'duelParticipant__away').text
      if "Avança na competição\n" in homeTeam:
        homeTeam = homeTeam.split("\n")[1]
      if "Avança na competição\n" in awayTeam:
        awayTeam = awayTeam.split("\n")[1]
      # detailScore__wrapper
      ht0g = driver.find_element(By.CLASS_NAME, 'detailScore__wrapper').text.split('-')[0].replace("\n", '')
      at0g = driver.find_element(By.CLASS_NAME, 'detailScore__wrapper').text.split('-')[1].replace("\n", '')
      round = driver.find_element(By.CLASS_NAME, 'tournamentHeader__country').text.split(' - ')[1]
      data_jogo = driver.find_element(By.CLASS_NAME, 'duelParticipant__startTime').text.split(' ')[0]
      estatisticas = driver.find_elements(By.CLASS_NAME, '_row_n1rcj_9')
      estatisticasPartida = []
      colunasPartidas = ['HomeTeam', 'AwayTeam']
      for i, field in enumerate(estatisticas):
        estatisticasPartida.append([field.text.split('\n')[0], field.text.split('\n')[1], field.text.split('\n')[2]])
        colunasPartidas.append(field.text.split('\n')[1])
      for i, coluna in enumerate(colunasEstatisticas[10:]):
          if coluna not in colunasPartidas:
              estatisticasPartida.insert(i, [0, coluna, 0])
      for i, coluna in enumerate(colunasPartidas):
          if coluna not in colunasEstatisticas:
              colunasPartidas.pop(i)
      if first_time:
          partidaLinha.append(data_jogo)
          partidaLinha.append(round)
          partidaLinha.append(homeTeam)
          partidaLinha.append(awayTeam)
          partidaLinha.append(ht0g)
          partidaLinha.append(at0g)
          partidaLinha.append(ht1g)
          partidaLinha.append(at1g)
          partidaLinha.append(ht2g)
          partidaLinha.append(at2g)
          first_time = False
      for estatistica in estatisticasPartida:
          if estatistica[1] in colunasEstatisticas:
              partidaLinha.append(estatistica[0])
              partidaLinha.append(estatistica[2])
    linhas.append(partidaLinha)
  df = pd.DataFrame(linhas, columns=colunasDataSet)
  df.to_csv(f"{nomeDataset}.csv")
  driver.quit()

