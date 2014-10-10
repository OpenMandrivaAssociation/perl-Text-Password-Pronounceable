%define upstream_name    Text-Password-Pronounceable
%define upstream_version 0.30

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Generate pronounceable passwords
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module generates pronuceable passwords, based the the English digraphs
by D Edwards.

METHODS
    * new($min, $max)

      Construct a password factory with length limits of $min and $max. If
      $max is omitted, it defaults to $min.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc CHANGES README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.300.0-2mdv2011.0
+ Revision: 656830
- rebuild for updated spec-helper

* Tue Aug 17 2010 Jérôme Quelin <jquelin@mandriva.org> 0.300.0-1mdv2011.0
+ Revision: 570933
- update to 0.30

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.280.0-1mdv2011.0
+ Revision: 471083
- import perl-Text-Password-Pronounceable


* Sun Nov 29 2009 cpan2dist 0.28-1mdv
- initial mdv release, generated with cpan2dist
