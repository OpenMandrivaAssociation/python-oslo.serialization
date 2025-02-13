Name:		python-oslo.serialization
Version:	5.6.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/o/oslo.serialization/oslo.serialization-%{version}.tar.gz
Summary:	Oslo Serialization library
URL:		https://pypi.org/project/oslo.serialization/
License:	None
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Oslo Serialization library

%files
%{py_sitedir}/oslo_serialization
%{py_sitedir}/oslo.serialization-*.*-info
