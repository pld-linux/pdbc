Summary:	pdb compiler/decompiler
Summary(pl):	pdb kompilator/dekompilator
Name:		pdbc
Version:	0.9.4
Release:	0.1
License:	GPL
Group:		Development/Building
Vendor:		Eric Obermuhlner
Source0:	%{name}-%{version}.tar.gz
URL:		http://www.obermuhlner.com/public/Projects/Palm/PDBC/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%prep
%setup -q -n %{name}-%{version}.orig -a 1
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
