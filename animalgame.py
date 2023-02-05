import random
import json
from enum import IntEnum

class Animal(IntEnum):
  """動物の種類"""
  KUMA = 1
  NEKO = 2
  USAGI = 3

class Jikan(IntEnum):
  """動物を育てる時間帯"""
  GOHAN = 1
  OHIRUNE = 2
  OHANASI = 3

class Nannido(IntEnum):
  """ゲームの難易度"""
  TEI = 1
  TYU = 2
  KOU = 3

class Chara:
  """ゲームを実行するキャラクター"""
  def __init__(self, syurui, serihufile):

    self.icon = ''
    self.sitsumon = []
    self.kotae = []
    self.tabeta_kaisu = 0
    self.ohirune_kaisu = 0
    self.ohanasi_kaisu = 0
    self.sodateta_kaisu = 0

    with open(serihufile) as f:
      jisyo = json.load(f)

    if syurui == Animal.KUMA:
      self.icon     = '🧸'
      self.sitsumon = jisyo["kuma"]["sitsumon"]
      self.kotae    = jisyo["kuma"]["kotae"]
    elif syurui == Animal.NEKO:
      self.icon     = '🐈'
      self.sitsumon = jisyo["neko"]["sitsumon"]
      self.kotae    = jisyo["neko"]["kotae"]
    elif syurui == Animal.USAGI:
      self.icon     = '🐇'
      self.sitsumon = jisyo["usa"]["sitsumon"]
      self.kotae    = jisyo["usa"]["kotae"]

  def get_icon(self):
    return self.icon

  def get_sitsumon(self, seed):
    return self.sitsumon[seed]

  def get_kotae(self, seed):
    return self.kotae[seed]

  def get_sitsumon_ikutu(self):
    return len(self.sitsumon)

  def get_kotae_ikutu(self):
    return len(self.kotae)

  def get_tabeta_kaisu(self):
    return self.tabeta_kaisu

  def get_ohirune_kaisu(self):
    return self.ohirune_kaisu

  def get_ohanasi_kaisu(self):
    return self.ohanasi_kaisu

  def get_sodateta_kaisu(self):
    return self.sodateta_kaisu

  def sodateru(self, jikan, seed):
    """作成したキャラを育てる"""
    self.sodateta_kaisu += 1
    if jikan == Jikan.GOHAN:
      self.tabeta_kaisu += 1
    elif jikan == Jikan.OHIRUNE:
      self.ohirune_kaisu += 1
    elif jikan == Jikan.OHANASI:
      self.ohanasi_kaisu += 1
    else:
      print('エラーです。初期化してください。')

  def get_point(self):
    """育成で取得したポイント"""
    return self.ohanasi_kaisu + self.tabeta_kaisu

def nannido_input():
  """ 難易度選択 """
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
  """ 動物選択 """
  syurui = int(input('動物を選択してください。[1=熊 2=猫 3=兎]：'))
  c = Chara(syurui)
  print(c.icon + " がうまれたよ")

def jikan_input():
  """ 飼育 """
  print('どんどんそだてましょー')
  jikan = int(input('1=ごはんの時間 2=おひるねの時間 3=お話する'))#intだと整数以外の入力NGなのでintはなくすでも変わんなかった

def game_syuryou():
  print('以下は、目安達成数値です。　# ・ohanasi: 低３　中15: 高30・gohan: 低３　中15: 高30・level: 低９　中250: 高1000')
  print('以下は、あなたの行動記録です。参考にしてまたぷれいしてくだいね')