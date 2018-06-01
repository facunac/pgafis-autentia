# contrib/wc/Makefile

MODULE_big = wc
OBJS = wc.o

EXTENSION = wc
DATA = wc--1.0.sql wc--unpackaged--1.0.sql

SHLIB_LINK = $(filter -lcrypt, $(LIBS))

ifdef USE_PGXS
PG_CONFIG = pg_config
PGXS := $(shell $(PG_CONFIG) --pgxs)
include $(PGXS)
else
subdir = contrib/wc
top_builddir = /usr/lib/postgresql/10/lib/pgxs
#top_builddir = ../..
include $(top_builddir)/src/Makefile.global
top_srcdir = /home/fac/fac/postgresql-10.4
include $(top_srcdir)/contrib/contrib-global.mk
endif
