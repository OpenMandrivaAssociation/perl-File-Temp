%define upstream_name    File-Temp
%define upstream_version 0.22

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(VMS::Stdio\\)'
%endif

Name:           perl-%{upstream_name}
Version:        %perl_convert_version %{upstream_version}
Release:        7

Summary:        Return name and handle of a temporary file safely
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{upstream_name}
Source0:        http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:      noarch

%description
File::Temp can be used to create and open temporary files in a safe way. There
is both a function interface and an object-oriented interface. The File::Temp
constructor or the tempfile() function can be used to return the name and the
open filehandle of a temporary file. The tempdir() function can be used to
create a temporary directory.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%install
%makeinstall_std

mv %{buildroot}%{_mandir}/man3/File::Temp.3pm \
    %{buildroot}%{_mandir}/man3/File::Temp-%{upstream_version}.3pm

%check
%__make test

%files 
%doc ChangeLog README
%{perl_vendorlib}/File
%{_mandir}/*/*



%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.220.0-5mdv2012.0
+ Revision: 765275
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.220.0-4
+ Revision: 764841
- rebuild

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.220.0-3
+ Revision: 763768
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.220.0-2
+ Revision: 667147
- mass rebuild

* Fri Jul 17 2009 Jérôme Quelin <jquelin@mandriva.org> 0.220.0-1mdv2010.1
+ Revision: 396809
- rebuild to have new automatic provides extraction
- using %%perl_convert_version
- fixed license field

* Tue Jun 30 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.22-1mdv2010.0
+ Revision: 390835
- update to new version 0.22

* Sun Nov 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.21-1mdv2009.1
+ Revision: 303773
- update to new version 0.21

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.20-3mdv2009.0
+ Revision: 223756
- rebuild

* Sat Dec 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.20-2mdv2008.1
+ Revision: 137220
- rename man page to avoid conflict with core

* Sat Dec 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.20-1mdv2008.1
+ Revision: 136772
- update to new version 0.20

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Nov 21 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.19-1mdv2008.1
+ Revision: 110874
- new version

* Fri Nov 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.18-1mdv2008.1
+ Revision: 105449
- import perl-File-Temp


* Fri Nov 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.18-1mdv2008.1
- first mdv release 
