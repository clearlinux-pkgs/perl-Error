#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Error
Version  : 0.17026
Release  : 16
URL      : https://www.cpan.org/authors/id/S/SH/SHLOMIF/Error-0.17026.tar.gz
Source0  : https://www.cpan.org/authors/id/S/SH/SHLOMIF/Error-0.17026.tar.gz
Summary  : 'Error/exception handling in an OO-ish way'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-2.0
Requires: perl-Error-doc
BuildRequires : perl(Module::Build)

%description
This archive contains the distribution Error,
version 0.17026:
Error/exception handling in an OO-ish way

%package doc
Summary: doc components for the perl-Error package.
Group: Documentation

%description doc
doc components for the perl-Error package.


%prep
%setup -q -n Error-0.17026

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/Error.pm
/usr/lib/perl5/site_perl/5.26.1/Error/Simple.pm

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/man/man3/*
