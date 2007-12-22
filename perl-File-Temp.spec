%define module  File-Temp
%define name    perl-%{module}
%define version 0.20
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Return name and handle of a temporary file safely
License:        GPL or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/File/%{module}-%{version}.tar.gz
Buildarch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
File::Temp can be used to create and open temporary files in a safe way. There
is both a function interface and an object-oriented interface. The File::Temp
constructor or the tempfile() function can be used to return the name and the
open filehandle of a temporary file. The tempdir() function can be used to
create a temporary directory.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%install
rm -rf %{buildroot}
%makeinstall_std

%check
%__make test

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc ChangeLog README
%{perl_vendorlib}/File
%{_mandir}/*/*

