#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Error
Version  : 0.17029
Release  : 36
URL      : https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/Error-0.17029.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/Error-0.17029.tar.gz
Summary  : 'Error/exception handling in an OO-ish way'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-2.0
Requires: perl-Error-license = %{version}-%{release}
Requires: perl-Error-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
This archive contains the distribution Error,
version 0.17029:
Error/exception handling in an OO-ish way

%package dev
Summary: dev components for the perl-Error package.
Group: Development
Provides: perl-Error-devel = %{version}-%{release}
Requires: perl-Error = %{version}-%{release}

%description dev
dev components for the perl-Error package.


%package license
Summary: license components for the perl-Error package.
Group: Default

%description license
license components for the perl-Error package.


%package perl
Summary: perl components for the perl-Error package.
Group: Default
Requires: perl-Error = %{version}-%{release}

%description perl
perl components for the perl-Error package.


%prep
%setup -q -n Error-0.17029
cd %{_builddir}/Error-0.17029

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Error
cp %{_builddir}/Error-0.17029/LICENSE %{buildroot}/usr/share/package-licenses/perl-Error/38e94f89ec602e1a6495ef7c30477d01aeefedc9
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Error.3
/usr/share/man/man3/Error::Simple.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Error/38e94f89ec602e1a6495ef7c30477d01aeefedc9

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.32.1/Error.pm
/usr/lib/perl5/vendor_perl/5.32.1/Error/Simple.pm
