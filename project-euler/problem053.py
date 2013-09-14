#!/usr/bin/env python3

########################################################################
#   Solves problem 53 from projectEuler.net.
#   Determines the amount of, not necessarily distinct, values of,
#   combinations of n taken by r for 1 n 100, are greater than one-million?
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

from CommonFunctions import factorial

if __name__ == '__main__':
    result = sum(1 for n in range(1, 101) for r in range(1, n+1) if
                 factorial(n) // factorial(r) // factorial(n-r) > 1000000)
    print("The result is:", result)