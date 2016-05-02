#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : uwsgi
Version  : 2.0.12
Release  : 11
URL      : http://projects.unbit.it/downloads/uwsgi-2.0.12.tar.gz
Source0  : http://projects.unbit.it/downloads/uwsgi-2.0.12.tar.gz
Source1  : uwsgi.tmpfiles
Source2  : uwsgi@.service
Source3  : uwsgi@.socket
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: uwsgi-bin
Requires: uwsgi-python
Requires: uwsgi-config
BuildRequires : greenlet-dev
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : setuptools
Patch1: async-profile.patch
Patch2: 0001-paste_loader-allow-specifying-alternative-section-na.patch

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


%package python
Summary: python components for the uwsgi package.
Group: Default

%description python
python components for the uwsgi package.


%prep
%setup -q -n uwsgi-2.0.12
%patch1 -p1
%patch2 -p1

%build
python2 setup.py build -b py2

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system/uwsgi@.service
install -m 0644 %{SOURCE3} %{buildroot}/usr/lib/systemd/system/uwsgi@.socket
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/tmpfiles.d/uwsgi.conf

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

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
