#
# source is actually under
# http://www.palmgear.com/software/redirector.cfm/pdbc_0.9.4.zip?prodID=29490&type=zip
# but since this url screws the filename I leave it url-less until someone
# wiser fixes this

Summary:	pdb compiler/decompiler
Summary(pl):	Kompilator/dekompilator pdb
Name:		pdbc
Version:	0.9.4
Release:	1
License:	GPL
Group:		Development/Building
Vendor:		Eric Obermuhlner
# renamed from http://www.palmgear.com/software/redirector.cfm/pdbc_0.9.4.zip?prodID=29490&type=zip
Source0:	%{name}_%{version}.zip
URL:		http://www.obermuhlner.com/public/Projects/Palm/PDBC/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pdb compiler/decompiler.

%description -l pl
Kompilator/dekompilator pdb.

%prep
%setup -q

%build
cd src
%{__make} CC="%{__cc} %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
