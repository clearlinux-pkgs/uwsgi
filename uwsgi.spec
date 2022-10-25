#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : uwsgi
Version  : 2.0.20
Release  : 83
URL      : https://github.com/unbit/uwsgi/archive/2.0.20/uwsgi-2.0.20.tar.gz
Source0  : https://github.com/unbit/uwsgi/archive/2.0.20/uwsgi-2.0.20.tar.gz
Source1  : uwsgi.tmpfiles
Source2  : uwsgi@.service
Source3  : uwsgi@.socket
Summary  : The uWSGI server
Group    : Development/Tools
License  : GPL-2.0
Requires: uwsgi-bin = %{version}-%{release}
Requires: uwsgi-config = %{version}-%{release}
Requires: uwsgi-filemap = %{version}-%{release}
Requires: uwsgi-lib = %{version}-%{release}
Requires: uwsgi-license = %{version}-%{release}
Requires: uwsgi-python = %{version}-%{release}
Requires: uwsgi-python3 = %{version}-%{release}
Requires: uwsgi-services = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi-greenlet-dev
BuildRequires : python3-dev
BuildRequires : python3-staticdev
Patch1: async-profile.patch
Patch2: build-plugins-flags.patch

%description
The uWSGI project
For official documentation check: https://uwsgi-docs.readthedocs.org/en/latest/

%package bin
Summary: bin components for the uwsgi package.
Group: Binaries
Requires: uwsgi-config = %{version}-%{release}
Requires: uwsgi-license = %{version}-%{release}
Requires: uwsgi-services = %{version}-%{release}
Requires: uwsgi-filemap = %{version}-%{release}

%description bin
bin components for the uwsgi package.


%package config
Summary: config components for the uwsgi package.
Group: Default

%description config
config components for the uwsgi package.


%package filemap
Summary: filemap components for the uwsgi package.
Group: Default

%description filemap
filemap components for the uwsgi package.


%package lib
Summary: lib components for the uwsgi package.
Group: Libraries
Requires: uwsgi-license = %{version}-%{release}
Requires: uwsgi-filemap = %{version}-%{release}

%description lib
lib components for the uwsgi package.


%package license
Summary: license components for the uwsgi package.
Group: Default

%description license
license components for the uwsgi package.


%package python
Summary: python components for the uwsgi package.
Group: Default
Requires: uwsgi-python3 = %{version}-%{release}

%description python
python components for the uwsgi package.


%package python3
Summary: python3 components for the uwsgi package.
Group: Default
Requires: uwsgi-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(uwsgi)

%description python3
python3 components for the uwsgi package.


%package services
Summary: services components for the uwsgi package.
Group: Systemd services

%description services
services components for the uwsgi package.


%prep
%setup -q -n uwsgi-2.0.20
cd %{_builddir}/uwsgi-2.0.20
%patch1 -p1
%patch2 -p1
pushd ..
cp -a uwsgi-2.0.20 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1664489928
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/uwsgi
cp %{_builddir}/uwsgi-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/uwsgi/ba8b424d462ab14f383ebc73adb43067c72e3a7f
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system/uwsgi@.service
install -m 0644 %{SOURCE3} %{buildroot}/usr/lib/systemd/system/uwsgi@.socket
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/tmpfiles.d/uwsgi.conf
## install_append content
PYTHON=python  %{buildroot}/usr/bin/uwsgi --build-plugin "plugins/python python"
install -d -m 755 %{buildroot}/usr/lib/uwsgi
install -p -D -m 644 python_plugin.so  %{buildroot}/usr/lib/uwsgi/


## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/uwsgi
/usr/share/clear/optimized-elf/bin*

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/uwsgi.conf

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-uwsgi

%files lib
%defattr(-,root,root,-)
/usr/lib/uwsgi/python_plugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/uwsgi/ba8b424d462ab14f383ebc73adb43067c72e3a7f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/uwsgi@.service
/usr/lib/systemd/system/uwsgi@.socket
