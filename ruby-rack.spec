#
# Conditional build:
%bcond_with	tests		# build without tests

%define	pkgname	rack
Summary:	Modular interface to webservers
Summary(pl.UTF-8):	Modularny interfejs do serwerów WWW
Name:		ruby-%{pkgname}
Version:	1.3.0
Release:	3
License:	MIT
Group:		Development/Libraries
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	765f523bb32c4475bfcb6898eddbc877
URL:		http://rubyforge.org/projects/rack
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
BuildRequires:	sed >= 4.0
%if %{with tests}
BuildRequires:	ruby-bacon
BuildRequires:	ruby-fcgi
BuildRequires:	ruby-memcache-client
BuildRequires:	ruby-mongrel
BuildRequires:	ruby-rake
BuildRequires:	ruby-thin
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rack provides a minimal, modular and adaptable interface for
developing web applications in Ruby. By wrapping HTTP requests and
responses in the simplest way possible, it unifies and distills the
API for web servers, web frameworks, and software in between (the
so-called middleware) into a single method call.

%description -l pl.UTF-8
Rack dostarcza minimalny, modularny i adaptowalny interfejs do
tworzenia aplikacji WWW w języku Ruby. Opakowując zapytania i
odpowiedzi HTTP w sposób najprostszy z możliwych, unifikuje oraz
przekształca API dla serwerów WWW, szkieletów aplikacji WWW i
oprogramowania znajdującego się między nimi (tzw. middleware) w jedno
wywołanie metody.

%package rdoc
Summary:	HTML documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla %{pkgname}
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
HTML documentation for %{pkgname}.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla %{pkgname}.

%package ri
Summary:	ri documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{pkgname}
Group:		Documentation
Requires:	ruby

%description ri
ri documentation for %{pkgname}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{pkgname}.

%prep
%setup -q -n %{pkgname}-%{version}
%{__sed} -i -e '1 s,#!.*ruby,#!%{__ruby},' bin/*

%build
# write .gemspec
%__gem_helper spec

rdoc --ri --op ri lib
rdoc --op rdoc lib
%{__rm} -r ri/{FCGI,created.rid,cache.ri}
%{__rm} ri/URI/cdesc-URI.ri

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{ruby_vendorlibdir},%{ruby_specdir},%{ruby_ridir},%{ruby_rdocdir}}

cp -a bin/* $RPM_BUILD_ROOT%{_bindir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a example/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README KNOWN-ISSUES COPYING
%attr(755,root,root) %{_bindir}/rackup
%{ruby_vendorlibdir}/rack.rb
%{ruby_vendorlibdir}/rack
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
%{_examplesdir}/%{name}-%{version}

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/Rack
