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
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pdb compiler/decompiler.

%description -l pl
Kompilator/dekompilator pdb.

%prep
%setup -q

%build
%{__make} -C src \
	CC="%{__cc} %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man{1,4}}

install src/pdbc.exe $RPM_BUILD_ROOT%{_bindir}/pdbc
install src/pdbdec.exe $RPM_BUILD_ROOT%{_bindir}/pdbdec
install man/man1/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
install man/man4/*.4 $RPM_BUILD_ROOT%{_mandir}/man4

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt html/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
