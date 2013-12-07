%define modname	File-Temp
%define modver	0.22

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(VMS::Stdio\\)'
%endif

Summary:	Return name and handle of a temporary file safely
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	11
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:	http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/File/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
File::Temp can be used to create and open temporary files in a safe way. There
is both a function interface and an object-oriented interface. The File::Temp
constructor or the tempfile() function can be used to return the name and the
open filehandle of a temporary file. The tempdir() function can be used to
create a temporary directory.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%install
%makeinstall_std

mv %{buildroot}%{_mandir}/man3/File::Temp.3pm \
	%{buildroot}%{_mandir}/man3/File::Temp-%{modver}.3pm

%check
%make test

%files 
%doc ChangeLog README
%{perl_vendorlib}/File
%{_mandir}/man3/*

