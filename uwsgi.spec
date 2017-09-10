#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : uwsgi
Version  : 2.0.15
Release  : 26
URL      : http://projects.unbit.it/downloads/uwsgi-2.0.15.tar.gz
Source0  : http://projects.unbit.it/downloads/uwsgi-2.0.15.tar.gz
Source1  : uwsgi.tmpfiles
Source2  : uwsgi@.service
Source3  : uwsgi@.socket
Summary  : The uWSGI server
Group    : Development/Tools
License  : GPL-2.0
Requires: uwsgi-bin
Requires: uwsgi-legacypython
Requires: uwsgi-config
Requires: uwsgi-lib
BuildRequires : go
BuildRequires : greenlet-dev
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
Patch1: async-profile.patch
Patch2: 0001-paste_loader-allow-specifying-alternative-section-na.patch
Patch3: 0001-plugins-corerouter-cr_map.c-fix-this-if-clause-does-.patch
Patch4: build-plugins-flags.patch

%description
The uWSGI project
For official documentation check: https://uwsgi-docs.readthedocs.org/en/latest/

%package bin
Summary: bin components for the uwsgi package.
Group: Binaries
Requires: uwsgi-config

%description bin
bin components for the uwsgi package.


%package config
Summary: config components for the uwsgi package.
Group: Default

%description config
config components for the uwsgi package.


%package legacypython
Summary: legacypython components for the uwsgi package.
Group: Default

%description legacypython
legacypython components for the uwsgi package.


%package lib
Summary: lib components for the uwsgi package.
Group: Libraries
Requires: uwsgi-config

%description lib
lib components for the uwsgi package.


%prep
%setup -q -n uwsgi-2.0.15
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1505073209
python2 setup.py build -b py2

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system/uwsgi@.service
install -m 0644 %{SOURCE3} %{buildroot}/usr/lib/systemd/system/uwsgi@.socket
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/tmpfiles.d/uwsgi.conf
## make_install_append content
PYTHON=python2.7  %{buildroot}/usr/bin/uwsgi --build-plugin "plugins/python python27"
PYTHON=python3.6  %{buildroot}/usr/bin/uwsgi --build-plugin "plugins/python python36"
install -d -m 755 %{buildroot}/usr/lib/uwsgi
install -p -D -m 644 python27_plugin.so  %{buildroot}/usr/lib/uwsgi/
install -p -D -m 644 python36_plugin.so  %{buildroot}/usr/lib/uwsgi/
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/uwsgi

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/uwsgi@.service
/usr/lib/systemd/system/uwsgi@.socket
/usr/lib/tmpfiles.d/uwsgi.conf

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files lib
%defattr(-,root,root,-)
/usr/lib/uwsgi/python27_plugin.so
/usr/lib/uwsgi/python36_plugin.so
