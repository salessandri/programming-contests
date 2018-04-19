//      3281.c
//      
//      Copyright 2010 Santiago Alessandri <salessandri@cert02>
//      
//      This program is free software; you can redistribute it and/or modify
//      it under the terms of the GNU General Public License as published by
//      the Free Software Foundation; either version 2 of the License, or
//      (at your option) any later version.
//      
//      This program is distributed in the hope that it will be useful,
//      but WITHOUT ANY WARRANTY; without even the implied warranty of
//      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//      GNU General Public License for more details.
//      
//      You should have received a copy of the GNU General Public License
//      along with this program; if not, write to the Free Software
//      Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
//      MA 02110-1301, USA.


#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static int team_arr[10][2];
static int prob_arr[10];
static int i, j, subs, test_case = 1, max = 0;

int main(int argc, char** argv)
{
	
    int teams, probs;
    
    scanf("%d %d", &teams, &probs);
    while (teams != 0) {
        for (i = 0; i < teams; i++) {
            for (j=0; j < 2; j++) {
                team_arr[i][j] = 0;
            }
        }
        for (i = 0; i < probs; i++) {
            scanf("%d", &prob_arr[i]);
        }
        scanf("%d", &subs);
        for (i = 0; i < subs; i++) {
            char p, r;
            int t, p2;
            scanf("%d %c %c", &t, &p, &r);
            t -= 1;
            p2 = p - 'A';
            if (r == 'A')
                team_arr[t][0] += prob_arr[p2];
            team_arr[t][1]++;
        }
        printf("%d\n", test_case++);
        for (i = 0; i < teams; i++) {
            for (j = 0; j < teams; j++) {
                if ((team_arr[j][0] > team_arr[max][0]) || ((team_arr[j][0] == team_arr[max][0]) && (team_arr[j][1] < team_arr[max][1])))
                    max = j;
            }
            printf("%d %d\n", max+1, team_arr[max][0]);
            team_arr[max][0] = -1;
        }
        scanf("%d %d", &teams, &probs);
    }
    
    
	return 0;
}
