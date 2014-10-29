Name: erloci
Version:0.0.2
Release:	1%{?dist}
Summary: Erlang Oracle OCI interface

Group:	Applications/System
License: Apache License v2
URL: http;//github.com/k2informatics/erloci
Source0: erloci-0.0.2.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
An Erlang driver for the Oracle OCI interface.
Ensure:
INSTANT_CLIENT_LIB_PATH = <path to oracle libs>
INSTANT_CLIENT_INCLUDE = <path to oracle include>
ERL_INTERFACE_DIR = <path to erlang erl-interface>

are set in the environment or included 
in c_src/Makefile.

To run the driver ensure and INSTANT_CLLIENT_LIB_PATH
are both set.

INSTANT_CLIENT_LIB_PATH = <path to oracle libs>
ORACLE_HOME = <path to oracle installation>

%prep
%setup -q


%build
./rebar compile

%install
echo %{buildroot}/usr/local/lib/erlang/lib/%{name}-%{version}
mkdir -p %{buildroot}/usr/local/lib/erlang/lib/%{name}-%{version}
cp -r ebin priv %{buildroot}/usr/local/lib/erlang/lib/%{name}-%{version}

%files
%define dir /usr/local/lib/erlang/lib
%defattr(-,root,root,-)
%{dir}/erloci-0.0.2/ebin/erloci.app
%{dir}/erloci-0.0.2/ebin/oci_app.beam
%{dir}/erloci-0.0.2/ebin/oci_logger.beam
%{dir}/erloci-0.0.2/ebin/oci_port.beam
%{dir}/erloci-0.0.2/ebin/oci_util.beam
%{dir}/erloci-0.0.2/priv/README
%{dir}/erloci-0.0.2/priv/liberloci.a
%{dir}/erloci-0.0.2/priv/ocierl

%changelog


