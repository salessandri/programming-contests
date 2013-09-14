#!/usr/bin/python3

########################################################################
#   Solves Google CodeJam 2009 Qualification Round's problem A
#   Copyright (C) 2011  Santiago Alessandri
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
#   Visit my wiki at http://wiki.san-ss.com.ar
#   Visit my blog at http://blog.san-ss.com.ar
########################################################################

last_letter = 'a'
W = 0
H = 0

def run_water(height_map, basin_map, i, j):
    global last_letter, H, W
    if basin_map[i][j]:
        return basin_map[i][j]
    min_h = height_map[i][j]
    direction = 0
    if i > 0 and height_map[i-1][j] < min_h:
        direction = 1
        min_h = height_map[i-1][j]
    if j > 0 and height_map[i][j-1] < min_h:
        direction = 2
        min_h = height_map[i][j-1]
    if j < W-1 and height_map[i][j+1] < min_h:
        direction = 3
        min_h = height_map[i][j+1]
    if i < H-1 and height_map[i+1][j] < min_h:
        direction = 4
        min_h = height_map[i+1][j]
    if direction == 0:
        basin_map[i][j] = last_letter
        last_letter = chr(ord(last_letter) + 1)
    elif direction == 1:
        basin_map[i][j] = run_water(height_map, basin_map, i-1, j)
    elif direction == 2:
        basin_map[i][j] = run_water(height_map, basin_map, i, j-1)
    elif direction == 3:
        basin_map[i][j] = run_water(height_map, basin_map, i, j+1)
    elif direction == 4:
        basin_map[i][j] = run_water(height_map, basin_map, i+1, j)
    return basin_map[i][j]

def solve():
    global last_letter, H, W
    H, W = map(int, input().split(' '))
    height_map = []
    for i in range(H):
        height_map.append(list(map(int, input().split(' '))))
    basin_map = [[''] * W for i in range(H)]
    last_letter = 'a'
    for i in range(H):
        for j in range(W):
            run_water(height_map, basin_map, i, j)
    for i in range(H):
        print(' '.join(basin_map[i]))

if __name__ == '__main__':
    T = int(input())
    for case in range(1, T+1):
        print("Case #{0}:".format(case))
        solve()
