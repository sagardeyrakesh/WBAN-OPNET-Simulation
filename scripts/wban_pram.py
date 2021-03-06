#!/usr/bin/env python
# -*- coding: utf-8 -*-

# user priority of packet
UP0 = '0'
UP1 = '1'
UP2 = '2'
UP3 = '3'
UP4 = '4'
UP5 = '5'
UP6 = '6'
UP7 = '7'
# data State - Generate, Queue Success, Sent, Receive
GEN = '0'
Q_SUCC = '1'
Q_FAIL = '2'
SENT = '3'
RCV = '4'
SUBQ = '5'
FAIL = '6'

# Max number of BAN coexist
MAX_BAN_NET = 16

# Network scenario
# sim_net = {'B1N4_sym': 0, 'B1N4_asym': 1, 'B2N8_sym': 2, 'B2N8_asym': 3}
sim_net = {'N4x1': '0', 'N4x2': '1'}
sim_scene = {'ver0_CSMA': '0', 'ver0_TDMA': '1', 'ver0_hybrid': '2',
             'ver1_hybrid': '3'}
sim_tf_mode = {'con': '0', 'exp': '1'}
