#
# Conditional build:
%bcond_with	tests		# build without tests

%define	pkgname	rack
Summary:	Modular interface to webservers
Summary(pl.UTF-8):	Modularny interfejs do serwerów WWW
Name:		ruby-%{pkgname}
Version:	3.2.5
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	ee7a83d79014045fef1d1ebde76e6d04
URL:		https://github.com/rack/rack
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
%if %{with tests}
BuildRequires:	ruby-minitest
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rack provides a minimal, modular and adaptable interface for
developing web applications in Ruby. By wrapping HTTP requests and
responses in the simplest way possible, it unifies and distills the
API for web servers, web frameworks, and software in between (the
so-called middleware) into a single method call.

Also, the rackup command has been moved to a separate gem called
rackup. Install that gem for the rackup command.

%description -l pl.UTF-8
Rack dostarcza minimalny, modularny i adaptowalny interfejs do
tworzenia aplikacji WWW w języku Ruby. Opakowując zapytania i
odpowiedzi HTTP w sposób najprostszy z możliwych, unifikuje oraz
przekształca API dla serwerów WWW, szkieletów aplikacji WWW i
oprogramowania znajdującego się między nimi (tzw. middleware) w jedno
wywołanie metody.

Polecenie rackup zostało przeniesione do osobnego gema o nazwie
rackup.

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

%build
# write .gemspec
%__gem_helper spec

rdoc --ri --op ri lib
rdoc --op rdoc lib
%{__rm} ri/created.rid
%{__rm} ri/cache.ri

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir},%{ruby_ridir},%{ruby_rdocdir}}

cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md MIT-LICENSE CHANGELOG.md CONTRIBUTING.md SPEC.rdoc
%{ruby_vendorlibdir}/rack.rb
%{ruby_vendorlibdir}/rack
%{ruby_specdir}/%{pkgname}-%{version}.gemspec

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/Rack
