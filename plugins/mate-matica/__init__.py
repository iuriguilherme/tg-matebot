# vim:fileencoding=utf-8
#  Plugin mate-matica para matebot: Mate Mática
#  Copyleft (C) 2019 Desobediente Civil, 2019 Matehackers, 2019 Velivery,
#    2019 Greatful
#  
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

import math, binascii, os

## π
def cmd_pi(args):
  try:
    tamanho = 51
    ## Eu não faço args['command_list'][0] pra evitar IndexError
    if ''.join(args['command_list']).isdigit():
      tamanho = int(''.join(args['command_list'])) + 2 ## Ignorar o '3.'
    constante = 4 * math.atan(1) ## Esta é uma boa aproximação de pi
    response = str(constante)[:tamanho]
    return {
      'status': True,
      'type': 'grupo',
      'response': response,
      'debug': u"pi calculado",
      'multi': False,
      'parse_mode': None,
      'reply_to_message_id': args['message_id'],
    }
  except Exception as e:
      return {
        'status': False,
        'type': 'erro',
        'response': u"Erro tentando calcular pi.",
        'debug': u"Pi falhou, exceção: %s" % (e),
        'multi': False,
        'parse_mode': None,
        'reply_to_message_id': args['message_id'],
      }

## φ
def cmd_phi(args):
  try:
    tamanho = 51
    ## Eu não faço args['command_list'][0] pra evitar IndexError
    if ''.join(args['command_list']).isdigit():
      tamanho = int(''.join(args['command_list'])) + 2 ## Ignorar o '1.'
    constante = ( 1 + math.sqrt(5) ) / 2 ## Esta é uma boa aproximação de phi
    response = str(constante)[:tamanho]
    return {
      'status': True,
      'type': 'grupo',
      'response': response,
      'debug': u"phi calculado",
      'multi': False,
      'parse_mode': None,
      'reply_to_message_id': args['message_id'],
    }
  except Exception as e:
      return {
        'status': False,
        'type': 'erro',
        'response': u"Erro tentando calcular phi.",
        'debug': u"Phi falhou, exceção: %s" % (e),
        'multi': False,
        'parse_mode': None,
        'reply_to_message_id': args['message_id'],
      }

## String hexadecimal suficientemente aleatória
def cmd_random(args):
  try:
    tamanho = 8
    ## Eu não faço args['command_list'][0] pra evitar IndexError
    if ''.join(args['command_list']).isdigit():
      tamanho = int(''.join(args['command_list']))
    aleatorio = binascii.hexlify(os.urandom(tamanho)).decode('utf-8')
    response = str(aleatorio)
    return {
      'status': True,
      'type': 'grupo',
      'response': response,
      'debug': u"Número aleatório gerado",
      'multi': False,
      'parse_mode': None,
      'reply_to_message_id': args['message_id'],
    }
  except Exception as e:
      return {
        'status': False,
        'type': 'erro',
        'response': u"Erro tentando gerar número aleatório.",
        'debug': u"Random falhou, exceção: %s" % (e),
        'multi': False,
        'parse_mode': None,
        'reply_to_message_id': args['message_id'],
      }

def cmd_r(args):
  return cmd_random(args)

