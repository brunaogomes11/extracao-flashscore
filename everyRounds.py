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
def get_data_from_tournament(pais, campeonato, ano, tempo):

  driver = webdriver.Chrome()
  driver.get("https://www.flashscore.com.br/futebol/inglaterra/campeonato-ingles/resultados/")
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
  partidaEst = {}
  colunasEstatisticas = ['HomeTeam', 'AwayTeam']
  colunasDataSet = ['HomeTeam', 'AwayTeam']
  linhas = []
  for i, field in enumerate(estatisticas):
    colunasDataSet.append(letras_maiusculas(field.text.split('\n')[1].replace('xG',''))+"HT1T")
    colunasDataSet.append(letras_maiusculas(field.text.split('\n')[1].replace('xG',''))+"AT1T")
    colunasEstatisticas.append(field.text.split('\n')[1])
  for j, id_partida in enumerate(id_partidas):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'duelParticipant__home')))
    driver.get(f'https://www.flashscore.com.br/jogo/{id_partida}/#/resumo-de-jogo/estatisticas-de-jogo/1')
    # Pegar Posse de bola 1° tempo - _value_1c6mj_5 _homeValue_1c6mj_10 
    # [[partida 1], [partida 2], [partida 3]...]
    homeTeam = driver.find_element(By.CLASS_NAME, 'duelParticipant__home').text
    awayTeam = driver.find_element(By.CLASS_NAME, 'duelParticipant__away').text
    estatisticas = driver.find_elements(By.CLASS_NAME, '_row_1csk6_9')
    estatisticasPartida = []
    colunasPartidas = ['HomeTeam', 'AwayTeam']
    for i, field in enumerate(estatisticas):
      estatisticasPartida.append([field.text.split('\n')[0],field.text.split('\n')[1],field.text.split('\n')[2]])
      colunasPartidas.append(field.text.split('\n')[1])
    for i, coluna in enumerate(colunasEstatisticas):
        if coluna not in colunasPartidas:
          estatisticasPartida.insert(i, [0, coluna, 0])
    partidaLinha = [homeTeam, awayTeam]
    for estatistica in estatisticasPartida:
      if (estatistica[1] != "Chutes Bloqueados"):
        partidaLinha.append(estatistica[0])
        partidaLinha.append(estatistica[2])
    if (len(partidaLinha)>38):
      print(homeTeam, awayTeam)
    linhas.append(partidaLinha)
  df = pd.DataFrame(linhas, columns=colunasDataSet)
  df.to_csv("PremierLeagueHT.csv")
  driver.quit()