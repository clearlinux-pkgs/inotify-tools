#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : inotify-tools
Version  : 3.20.1
Release  : 4
URL      : https://github.com/rvoicilas/inotify-tools/archive/3.20.1.tar.gz
Source0  : https://github.com/rvoicilas/inotify-tools/archive/3.20.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: inotify-tools-bin
Requires: inotify-tools-lib
Requires: inotify-tools-license
Requires: inotify-tools-man

%description
inotify-tools
=============
This is a package of some commandline utilities relating to inotify.

%package bin
Summary: bin components for the inotify-tools package.
Group: Binaries
Requires: inotify-tools-license
Requires: inotify-tools-man

%description bin
bin components for the inotify-tools package.


%package dev
Summary: dev components for the inotify-tools package.
Group: Development
Requires: inotify-tools-lib
Requires: inotify-tools-bin
Provides: inotify-tools-devel

%description dev
dev components for the inotify-tools package.


%package lib
Summary: lib components for the inotify-tools package.
Group: Libraries
Requires: inotify-tools-license

%description lib
lib components for the inotify-tools package.


%package license
Summary: license components for the inotify-tools package.
Group: Default

%description license
license components for the inotify-tools package.


%package man
Summary: man components for the inotify-tools package.
Group: Default

%description man
man components for the inotify-tools package.


%prep
%setup -q -n inotify-tools-3.20.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1533837479
%reconfigure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1533837479
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/inotify-tools
cp COPYING %{buildroot}/usr/share/doc/inotify-tools/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/inotifywait
/usr/bin/inotifywatch

%files dev
%defattr(-,root,root,-)
/usr/include/inotifytools/inotify-nosys.h
/usr/include/inotifytools/inotify.h
/usr/include/inotifytools/inotifytools.h
/usr/lib64/libinotifytools.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libinotifytools.so.0
/usr/lib64/libinotifytools.so.0.4.1

%files license
%defattr(-,root,root,-)
/usr/share/doc/inotify-tools/COPYING

%files man
%defattr(-,root,root,-)
/usr/share/man/man1/inotifywait.1
/usr/share/man/man1/inotifywatch.1
