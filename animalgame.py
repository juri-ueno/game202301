import random
import json
import Enum

class Animal(IntEnum):
  KUMA = 1
  NEKO = 2
  USAGI = 3

class Jikan(IntEnum):
  GOHAN = 1
  OHIRUNE = 2
  OHANASI = 3

class Nannido(IntEnum):
  TEI = 1
  TYU = 2
  KOU = 3

class Chara(syurui, serihu)
  icon
  sitsumon
  kotae
  tabeta_kaisu
  ohanasi_kaisu
  point

  def __init__(self, syurui):

    jisyo = {}
    with open("animalserihu.txt", mode="r") as serihufile:
      jisyo = json.load(serihufile)

    if syurui == Animal.KUMA
      icon = '🧸'
      sitsumon = jisyo.kuma.sitsumon
      kotae    = jisyo.kuma.kotae
    elif syurui == Animal.NEKO
      icon = '🐈'
      sitsumon = jisyo.neko.sitsumon
      kotae    = jisyo.neko.kotae
    elif syurui == Animal.USAGI
      icon = '🐇'
      sitsumon = jisyo.usa.sitsumon
      kotae    = jisyo.usa.kotae
    print(icon + "がうまれたよ")

  def sodateru(jikan):
    """作成したキャラを育てる"""
    sitsumon_ikutu = len(sitsumon)
    kotae_ikutu    = len(kotae)

    if jikan == Jikan.GOHAN:
      print(sitsumon[random.randint(0, sitsumon_ikutu)] + '?')
      print(kotae   [random.randint(0, kotae_ikutu)])
      tabeta_kaisu += 1
      point = ohanasi_kaisu * tabeta_kaisu
      return point
    elif jikan == Jikan.OHIRUNE:
      print('むにゃむにゃ．．．')
      return point
    elif jikan == Jikan.OHANASI:
      print(sitsumon[random.randint(0, sitsumon_ikutu)] + '?')
      print(kotae   [random.randint(0, kotae_ikutu)])
      ohanasi_kaisu += 1
      point=nohanasi_kaisu * tabeta_kaisu
      return point
    else:
      print('エラーです。初期化してください。')

    
def nannido_input():
  """難易度選択"""
  nannido=int(input('難易度は？[1=低 2=中 3=高]:'))
  if nannido == Nannido.TEI:
    level=9
    print('低ですね。楽しんでください')
  elif nannido == Nannido.TYU:
    level=250
    print('中ですね。おすすめです。')
  elif nannido == Nannido.KOU:
    level=1000
    print('高ですか頑張ってください(^▽^)/')
  else:
    print('エラーです。やり直してください。')

def chara_input():
  """動物選択"""
  syurui=int(input('動物を選択してください。[1=熊 2=猫 3=兎]：'))
  c = Chara(syurui)

def jikan_input():
  """飼育"""
  print('どんどんそだてましょー')
  jikan=int(input('1=ごはんの時間 2=おひるねの時間 3=お話する'))#intだと整数以外の入力NGなのでintはなくすでも変わんなかった

def game_syuryou():
  print('以下は、目安達成数値です。　# ・ohanasi: 低３　中15: 高30・gohan: 低３　中15: 高30・level: 低９　中250: 高1000')
  print('以下は、あなたの行動記録です。参考にしてまたぷれいしてくだいね')