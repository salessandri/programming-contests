#!/usr/bin/env python3

########################################################################
#   Solves problem 17 from projectEuler.net.
#   Finds how many characters are needed to write all numbers from one
#   to one thousand in English.
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
#   You can contact me at san.lt.ss@gmail.com
#   Visit my wiki at http://san-ss.wikidot.com
########################################################################

def one_number_decoder(n):
    if n == '0':
        return 0
    if n == '1':
        return 3
    if n == '2':
        return 3
    if n == '3':
        return 5
    if n == '4':
        return 4
    if n == '5':
        return 4
    if n == '6':
        return 3
    if n == '7':
        return 5
    if n == '8':
        return 5
    if n == '9':
        return 4

def two_number_decoder(n):
    
    x = n[0]
    y = n[1]
    if x == '0':
        return one_number_decoder(n[1])
    if x == '1':
        if y == '0':
            return 3
        if y == '1':
            return 6
        if y == '2':
            return 6
        if y == '3':
            return len('thriteen')
        if y == '4':
            return len('fourteen')
        if y == '5':
            return len('fifteen')
        if y == '6':
            return len('sixteen')
        if y == '7':
            return len('seventeen')
        if y == '8':
            return len('eighteen')
        if y == '9':
            return len('nineteen')
    if x == '2':
        res = len('twenty')
    if x == '3':
        res = len('thrity')
    if x == '4':
        res = len('forty')
    if x == '5':
        res = len('fifty')
    if x == '6':
        res = len('sixty')
    if x == '7':
        res = len('seventy')
    if x == '8':
        res = len('eighty')
    if x == '9':
        res = len('ninety')
    return res + one_number_decoder(y)

def three_number_decoder(n):
    x = n[0]

    res = one_number_decoder(x)
    res += len('hundred')

    additional = two_number_decoder(n[1:3])
    if additional > 0:
        res += 3 #Adding 'and' word
    res += additional
    return res

if __name__ == '__main__':
    result = 0
    for n in range(1,1000):
        if n < 10:
            result += one_number_decoder(str(n))
        if n >= 10 and n < 100:
            result += two_number_decoder(str(n))
        if n >= 100 and n < 1000:
            result += three_number_decoder(str(n))
    result += len('onethousand')
    print("The result is:", result)
