def longShort(name):
	longShort = [
				[	'TenGigabitEthernet'	,	'te'	],
				[	'GigabitEthernet'		,	'gi'	],
				[	'FastEthernet'			,	'fa'	],
				[	'Loopback'				,	'lo'	],
				[	'Ethernet'				,	'e'		],
				[	'Vlan'					,	'vl'	],
				[	'Port-channel'			,	'po'	],
				[	'Tunnel'				,	'tu'	]
				]

	for short in longShort:
		name = name.replace(short[0],short[1])
	
	return name