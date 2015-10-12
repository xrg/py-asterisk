%define git_repo python-Asterisk

#define distsuffix xrg

Name:       python-Asterisk
Summary:    Asterisk Manager API Python interface
Version:    %git_get_ver
Release:    %mkrel %git_get_rel
URL:        http://code.google.com/p/py-asterisk/
Source0:    %git_bs_source %{name}-%{version}.tar.gz
License:    MIT
BuildArch:  noarch
Group:      Libraries
BuildRequires:  python
%py_requires -d

%description
Python API binding for Asterisk Manager Interface (AMI)


%prep
%git_get_source
%setup -q
find . -type f | xargs perl -p -i -e 's@#!/bin/env python@#!/usr/bin/env python@'

%build
python setup.py build

%install
python setup.py install --root=%{buildroot} --compile
# --optimize=2

# Note: don't let that script pollute /usr/bin . Instead, leave it in doc dir.
install -d %{buildroot}%{_defaultdocdir}/%{name}/examples/
mv %{buildroot}%{_bindir}/asterisk-dump  %{buildroot}%{_bindir}/py-asterisk \
        %{buildroot}%{_defaultdocdir}/%{name}/examples/


%files
%defattr(-,root,root)
# doc README.html HISTORY.html
%{py_sitedir}/*
%{_defaultdocdir}/%{name}/examples/

