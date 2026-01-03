#
# Conditional build:
%bcond_without	tests	# unit tests

%define		pdir	Class
%define		pnam	Unload
Summary:	Class::Unload - unload a class
Summary(pl.UTF-8):	Class::Unload - wyładowanie klasy
Name:		perl-Class-Unload
Version:	0.12
Release:	1
# same as perl 5
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Class/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a1fb61fb984184d4a939e33f6973a7af
URL:		https://metacpan.org/dist/Class-Unload
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Class-Inspector
BuildRequires:	perl-Test-Requires
BuildRequires:	perl-Test-Simple >= 0.88
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Unloads the given class by clearing out its symbol table and removing
it from INC hash.

%description -l pl.UTF-8
Moduł wyładowuje podaną klasę czyszcząc jego tablicę symboli i
usuwając ją z hasza INC.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Class/Unload.pm
%{_mandir}/man3/Class::Unload.3pm*
