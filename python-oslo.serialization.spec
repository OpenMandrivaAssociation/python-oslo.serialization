%define module oslo_serialization

Name:		python-oslo.serialization
Version:	5.9.1
Release:	1
Summary:	Oslo Serialization library
License:	None
Group:		Development/Python
URL:		https://pypi.org/project/oslo.serialization/
Source0:	https://files.pythonhosted.org/packages/source/o/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pbr)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
Oslo Serialization library

%files
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}.dist-info
