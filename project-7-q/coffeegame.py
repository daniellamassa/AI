import sys
from contextlib import closing

import numpy as np
from six import StringIO, b

from typing import Optional
from gym import Env, spaces, utils
from gym.envs.toy_text.utils import categorical_sample
from gym.error import DependencyNotInstalled
#from gym import utils
#from gym.envs.toy_text import discrete

LEFT = 0
DOWN = 1
RIGHT = 2
UP = 3

MAPS = {
    "3x3": [
        "SCH",
        "DHC",
        "HHG",
    ]}



class CoffeeEnv(Env):

    metadata = {'render.modes': ['human', 'ansi']}

    def __init__(self, desc=None, map_name="3x3",is_slippery=True):
        if desc is None and map_name is None:
            desc = generate_random_map()
        elif desc is None:
            desc = MAPS[map_name]
        self.desc = desc = np.asarray(desc,dtype='c')
        self.nrow, self.ncol = nrow, ncol = desc.shape
        self.reward_range = (0, 1)


        nA = 4
        nS = nrow * ncol

        self.s = 0
        self.lastaction = None

        self.observation_space = spaces.Discrete(nS)
        self.action_space = spaces.Discrete(nA)

        isd = np.array(desc == b'S').astype('float64').ravel()
        isd /= isd.sum()

        #generate transition table
        self.P = {s : {a : [] for a in range(nA)} for s in range(nS)}
        Rewards = {b'S':-1,b'G':10, b'H':-1,b'D':-10,b'C':1}

        def to_s(row, col):
            return row*ncol + col

        def inc(row, col, a):
            if a == LEFT:
                col = max(col-1,0)
            elif a == DOWN:
                row = min(row+1,nrow-1)
            elif a == RIGHT:
                col = min(col+1,ncol-1)
            elif a == UP:
                row = max(row-1,0)
            return (row, col)

        for row in range(nrow):
            for col in range(ncol):
                s = to_s(row, col)
                for a in range(4):
                    li = self.P[s][a]
                    letter = desc[row, col]
                    #if letter in b'C':
                    #    li.append((1.0, s, 0, True))
                    #elif letter in b'H':
                    #    li.append((-1.0, s, 0, True))
                    #else:
                    newrow, newcol = inc(row, col, a)
                    newstate = to_s(newrow, newcol)
                    newletter = desc[newrow, newcol]
                    done = bytes(newletter) in b'DG'
                    rew = Rewards[newletter]
                    li.append((1.0, newstate, rew, done))

        #super(CoffeeEnv, self).__init__(nS, nA, P, isd)
        super(CoffeeEnv, self).__init__()

    def reset( self, *,
        seed: Optional[int] = None,
        return_info: bool = False,
        options: Optional[dict] = None,
    ):
        super().reset(seed=seed)
        self.s = 0
        self.lastaction = None

        if not return_info:
            return int(self.s)
        else:
            return int(self.s), {"prob": 1}

    def step(self, a):
        transitions = self.P[self.s][a]
        i = categorical_sample([t[0] for t in transitions], self.np_random)
        p, s, r, d = transitions[i]
        self.s = s
        self.lastaction = a
        print(p,s,r,d)
        if d:
            self.reset()
        return (int(s), r, d, {"prob": p})

    def render(self, mode='human'):
        outfile = StringIO() if mode == 'ansi' else sys.stdout

        row, col = self.s // self.ncol, self.s % self.ncol
        desc = self.desc.tolist()
        desc = [[c.decode('utf-8') for c in line] for line in desc]
        desc[row][col] = utils.colorize(desc[row][col], "red", highlight=True)
        if self.lastaction is not None:
            outfile.write("  ({})\n".format(["Left","Down","Right","Up"][self.lastaction]))
        else:
            outfile.write("\n")
        outfile.write("\n".join(''.join(line) for line in desc)+"\n")

        if mode != 'human':
            with closing(outfile):
                return outfile.getvalue()