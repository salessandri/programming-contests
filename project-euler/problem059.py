#!/usr/bin/env python3

########################################################################
#   Solves problem 59 from projectEuler.net.
#   Finds the key to decipher a xor encrypted text.
#   Copyright (C) 2010  Santiago Alessandri
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#    
#   You can contact me at san.lt.ss@gmail.com or salessandri@nasel.com
#   Visit my wiki at http://san-ss.wikidot.com
########################################################################

def valid_char(x):
    if (x >= 32 and x <= 34):
        return True
    if (x >= 39 and x <= 46):
        return True
    if (x >= 58 and x <= 59):
        return True
    return chr(x).isalnum()

if __name__ == '__main__':
    f = open("cipher1.txt")
    chars = [int(c) for c in f.read().split(',')]
    f.close()
    
    chars_per_key = [[],[],[]]
    for i in range(len(chars)):
        chars_per_key[i % 3].append(chars[i])
    
    valid_keys = [[],[],[]]
    for k in range(ord('a'), ord('z')+1):
        for i in range(3):
            decoded = filter(valid_char, map(lambda x: k ^ x, chars_per_key[i]))
            if sum(1 for _ in decoded) == len(chars_per_key[i]):
                valid_keys[i].append(k)
    
    for k1 in valid_keys[0]:
        for k2 in valid_keys[1]:
            for k3 in valid_keys[2]:
                key = (k1, k2, k3)
                suma = 0
                decoded_text = ''
                for i in range(len(chars)):
                    decoded_char = chars[i] ^ key[i % 3]
                    decoded_text += chr(decoded_char)
                    suma += decoded_char
                print("Possible solution (",
                      ''.join(map(chr,  key)),
                      ",",
                      suma,
                      "):",
                      decoded_text
                      )
                print("------------")

