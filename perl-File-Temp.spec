%define upstream_name    File-Temp
%define upstream_version 0.22

Name:           perl-%{upstream_name}
Version:        %perl_convert_version %{upstream_version}
Release:        %mkrel 1

Summary:        Return name and handle of a temporary file safely
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{upstream_name}
Source0:        http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.gz

Buildarch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

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
rm -rf %{buildroot}
%makeinstall_std

mv %{buildroot}%{_mandir}/man3/File::Temp.3pm \
    %{buildroot}%{_mandir}/man3/File::Temp-%{upstream_version}.3pm

%check
%__make test

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc ChangeLog README
%{perl_vendorlib}/File
%{_mandir}/*/*

