
-- #####################################################################
--  Solves problem 158 from projectEuler.net.
--  Finds maximum number of combinations of strings that only have one
--  character bigger than the one to its left.
--  Copyright (C) 2011  Santiago Alessandri
--
--  This program is free software: you can redistribute it and/or modify
--  it under the terms of the GNU General Public License as published by
--  the Free Software Foundation, either version 3 of the License, or
--  (at your option) any later version.
--
--  This program is distributed in the hope that it will be useful,
--  but WITHOUT ANY WARRANTY; without even the implied warranty of
--  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
--  GNU General Public License for more details.
--
--  You should have received a copy of the GNU General Public License
--  along with this program. If not, see <http://www.gnu.org/licenses/>.
--	
--  You can contact me at san.lt.ss@gmail.com
--  Visit my wiki at http://wiki.san-ss.com.ar
--  Visit my blog at http://blog.san-ss.com.ar
-- #####################################################################

import Data.Map
import Data.Maybe

factorial n = factorial' n 1
    where
        factorial' n res
            | n < 2 = res
            | n >= 2 = factorial' (n-1) (res * n)

comb x y = ((factorial x) `div` ((factorial y) * (factorial (x-y))))

getValue :: (Integer, Integer, Integer) -> Map (Integer, Integer, Integer) Integer -> (Integer, Map (Integer, Integer, Integer) Integer )
getValue (length, greater, count) dp
    | count > 1 = (0, dp)
    | member (length, greater, count) dp = (fromJust (Data.Map.lookup (length, greater, count) dp), dp)
    | notMember (length, greater, count) dp = getValue' (length, greater, count) dp 0 0
        where
            getValue' (length, greater, count) dp i res
                | i == length = (res, insert (length, greater, count) res dp)
                | i < length = getValue' (length, greater, count) nDp (i+1) (res + nRes)
                where
                    nCount = if i < greater then count+1 else count
                    (nRes, upDp) = getValue ((length -1), i, nCount) dp
                    nDp = insert ((length -1), i, nCount) nRes dp

p :: Integer -> Map (Integer, Integer, Integer) Integer -> (Integer, Map (Integer, Integer, Integer) Integer)
p n dp = p' 0 dp 0
    where
        p' x dp res 
            | x == n = (res * (comb 26 n), dp)         
            | x < n  = p' (x + 1) nDp (res + nRes)
            where
                (nRes, nDp) = getValue ((n-1), x, 0) dp

initialDp = fromList [((0,0,0), 0), ((0,0,1), 1)]

main = print ("The result is: " ++ (show (first (foldl f (0, initialDp) [1..26]))))
    where
        first (x, y) = x
        f (r, dp) n = 
            let
                (nRes, nDp) = p n dp
                maxR = max r nRes
            in
                (maxR, nDp)
