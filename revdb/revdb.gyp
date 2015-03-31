{
	'includes':
	[
		'../common.gypi',
	],
	
	'targets':
	[
		{
			'target_name': 'dbmysql',
			'type': 'loadable_module',
			'mac_bundle': 1,
			
			'dependencies':
			[
				'../libexternal/libexternal.gyp:libExternal',
				'../thirdparty/libmysql/libmysql.gyp:libmysql',
				'../thirdparty/libopenssl/libopenssl.gyp:libopenssl',
				'../thirdparty/libz/libz.gyp:libz',
			],
			
			'include_dirs':
			[
				'src',
			],
			
			'sources':
			[
				'src/dbdrivercommon.cpp',
				'src/database.cpp',
				'src/dbmysqlapi.cpp',
				'src/mysql_connection.cpp',
				'src/mysql_cursor.cpp',
			],
			
			'xcode_settings':
			{
				'INFOPLIST_FILE': 'rsrc/dbmysql-Info.plist',
			},
		},
		{
			'target_name': 'dbodbc',
			'type': 'loadable_module',
			'mac_bundle': 1,
			
			# Not for Windows
			'conditions':
			[
				[
					'OS == "win"',
					{
						'type': 'none',
					},
				],
			],
			
			'dependencies':
			[
				'../libexternal/libexternal.gyp:libExternal',
				'../thirdparty/libiodbc/libiodbc.gyp:libiodbc',
			],
			
			'include_dirs':
			[
				'src',
			],
			
			'sources':
			[
				'src/dbdrivercommon.cpp',
				'src/database.cpp',
				'src/dbodbcapi.cpp',
				'src/odbc_connection.cpp',
				'src/odbc_cursor.cpp',
			],
			
			'xcode_settings':
			{
				'INFOPLIST_FILE': 'rsrc/dbodbc-Info.plist',
			},
		},
		{
			'target_name': 'dbpostgresql',
			'type': 'loadable_module',
			'mac_bundle': 1,
			
			'dependencies':
			[
				'../libexternal/libexternal.gyp:libExternal',
				'../thirdparty/libpq/libpq.gyp:libpq',
			],
			
			'include_dirs':
			[
				'src',
			],
			
			'sources':
			[
				'src/dbdrivercommon.cpp',
				'src/database.cpp',
				'src/dbpostgresqlapi.cpp',
				'src/postgresql_connection.cpp',
				'src/postgresql_cursor.cpp',
			],
			
			'xcode_settings':
			{
				'INFOPLIST_FILE': 'rsrc/dbpostgresql-Info.plist',
			},
		},
		{
			'target_name': 'dbsqlite',
			'type': 'loadable_module',
			'mac_bundle': 1,
			
			'dependencies':
			[
				'../libexternal/libexternal.gyp:libExternal',
				'../thirdparty/libsqlite/libsqlite.gyp:libsqlite',
			],
			
			'include_dirs':
			[
				'src',
			],
			
			'sources':
			[
				'src/dbdrivercommon.cpp',
				'src/database.cpp',
				'src/dbsqliteapi.cpp',
				'src/sqlite_connection.cpp',
				'src/sqlite_cursor.cpp',
			],
			
			'xcode_settings':
			{
				'INFOPLIST_FILE': 'rsrc/dbsqlite-Info.plist',
				'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
			},
		},
		{
			'target_name': 'revdb',
			'type': 'loadable_module',
			'mac_bundle': 1,
			
			'dependencies':
			[
				'../libcore/libcore.gyp:libCore',
				'../libexternal/libexternal.gyp:libExternal',
			],
			
			'include_dirs':
			[
				'src',
			],
			
			'sources':
			[
				'src/revdb.cpp',
				'src/osxsupport.cpp',
				'src/unxsupport.cpp',
				'src/w32support.cpp',
				'src/database.cpp',
				'src/dbdrivercommon.cpp',
			],
			
			'xcode_settings':
			{
				'INFOPLIST_FILE': 'rsrc/revdb-Info.plist',
			},
		},
	],
}
