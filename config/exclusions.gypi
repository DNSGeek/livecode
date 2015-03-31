{
	# Patterns to exclude platform-specific files
	'target_defaults':
	{
		'conditions':
		[
			[
				'OS != "win"',
				{
					'sources/':
					[
						['exclude', '_w32\\.cpp$'],
						['exclude', '(^|/)w32.+\\.cpp$'],
					],
				},
				{
					'sources/':
					[
						['exclude', '_posix\\.cpp$'],
					],
				},
			],
			[
				'OS != "mac"',
				{
					'sources/':
					[
						['exclude', '_osx\\.cpp$'],
						['exclude', '(^|/)osx.+\\.cpp$'],
					],
				},
			],
			[
				'OS != "linux"',
				{
					'sources/':
					[
						['exclude', '_lnx\\.cpp$'],
						['exclude', '(^|/)lnx.+\\.cpp$'],
						['exclude', '(^|/)unx.+\\.cpp$'],
					],
				},
			],
			[
				'OS != "android"',
				{
					'sources/':
					[
						['exclude', '_android.cpp$'],
						['exclude', '(^|/)mblandroid.*\\.cpp$'],
						['exclude', '\\.java$'],
					],
				},
			],
			[
				'OS != "ios"',
				{
					'sources/':
					[
						['exclude', '_ios\\.(cpp|mm)$'],
						['exclude', '(^|/)mbliphone.*\\.(cpp|mm)$'],
					],
				},
			],
			[
				'OS != "android" and OS != "ios"',
				{
					'sources/':
					[
						['exclude', '(^|/)mbl.+\\.cpp$'],
					],
				},
			],
			[
				'OS != "mac" and OS != "ios"',
				{
					'sources/':
					[
						['exclude', '\\.m(m?)$'],
					],
				},
			],
		],
	},
}
