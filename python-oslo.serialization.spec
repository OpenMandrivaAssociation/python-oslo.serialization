Name:		python-oslo.serialization
Version:	5.9.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/o/oslo_serialization/oslo_serialization-%{version}.tar.gz
Summary:	Oslo Serialization library
URL:		https://pypi.org/project/oslo.serialization/
License:	None
Group:		Development/Python
BuildRequires:	python
BuildRequires:	python%{pyver}dist(pbr)
BuildSystem:	python
BuildArch:	noarch

%description
Oslo Serialization library

%files
%{py_sitedir}/oslo_serialization
%{py_sitedir}/oslo_serialization-%{version}.dist-info
