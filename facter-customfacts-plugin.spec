%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define release %{rpm_release}%{?dist}

Summary: CustomFacts plugin for Facter
Name: facter-customfacts-plugin
Version: %{version}
Release: %{release}
Group: System Tools
License: Apache v2
URL: https://launchpad.net/ubuntu/oneiric/+package/facter-customfacts-plugin
Source0: %{name}-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: ruby
Requires: facter
Packager: Jay Klehr <jay@diablomedia.com>
BuildArch: noarch

%description
Facter plugin that reads facts from individual files stored in facts dir

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
%{__install} -d -m0755  %{buildroot}/%{ruby_sitelib}/facter
%{__install} -d -m0755  %{buildroot}/etc/facts
%{__install} -d -m0755  %{buildroot}/usr/bin
%{__install} -m0644 usr/lib/ruby/1.8/facter/customfacts.rb %{buildroot}/%{ruby_sitelib}/facter
%{__install} -m0755 usr/bin/fact-add %{buildroot}/usr/bin/fact-add
%{__install} -m0755 usr/bin/fact-del %{buildroot}/usr/bin/fact-del

%clean
rm -rf %{buildroot}

%post

%preun

%postun

%files
%{ruby_sitelib}/facter/customfacts.rb
/usr/bin/fact-add
/usr/bin/fact-del

%changelog
* Fri Sep 16 2011 Jay Klehr <jay@diablomedia.com> - 1.0.0
- First release

