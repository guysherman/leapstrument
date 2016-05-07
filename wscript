#! /usr/bin/env python
# encoding: utf-8
# Guy Sherman, 2015

import subprocess
import waftools
import os

LEAPSTRUMENT_VERSION			=	'0.0.1'
LEAPSTRUMENT_MAJOR_VERSION 		=	'0'


VERSION = LEAPSTRUMENT_VERSION
APPNAME = 'leapstrument'

top = '.'
out = 'build'
libs = ['']
lib_dirs = [os.environ['LEAP_SDK_HOME']+'/lib']
static_libs = ['']
static_lib_dirs = ['']
includes = [os.environ['LEAP_SDK_HOME']+'/include']
defines = ''


SUBFOLDERS = ['dep']

def options(opt):
	#opt.recurse(SUBFOLDERS)

	opt.load('compiler_cxx')
	#opt.load('cppcheck', tooldir=waftools.location)
	#opt.add_option("--shared", action="store_true", help="build shared library")
	#opt.add_option("--static", action="store_true", help="build static library")


def configure(conf):
	env = conf.env
	#conf.recurse(SUBFOLDERS)
	conf.setenv('leapstrument', env)
	conf.load('compiler_cxx')
	conf.env.CXXFLAGS = ['-Wall', '-ansi', '-ggdb']
	#conf.env.LIBPATH = lib_dirs
	#conf.env.STLIBPATH = static_lib_dirs
	#conf.env.INCLUDES = includes
	conf.check(header_name='Leap.h', features='c cprogram cxx cxxprogram', includes=includes)
	conf.check(header_name='jack/jack.h', features='c cprogram cxx cxxprogram', includes=includes)

	conf.write_config_header('config.h')
def build(bld):
	bld.env = bld.all_envs['leapstrument']
	#bld.program(source = bld.path.ant_glob('src/**/*.cxx'),
	bld.program(source = 'src/jack_main.cxx',
				includes = includes,
				cxxflags=['-w'],
				lib = ['jack'],
				target = 'leapstrument_jack',
				install_path = '${BINDIR}',
				defines = defines,
				#use=['oca', 'wq', 'gtest', 'gtest_main'],
				)
