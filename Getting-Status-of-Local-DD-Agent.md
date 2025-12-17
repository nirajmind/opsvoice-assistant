# Getting status of the DD agent running locally 


PS C:\WINDOWS\system32> & "C:\Program Files\Datadog\Datadog Agent\bin\agent.exe" status

Getting the status from the agent.

===============
Agent (v7.73.0)
===============
  Status date: 2025-12-17 10:06:36.554 +04 / 2025-12-17 06:06:36.554 UTC (1765951596554)
  Agent start: 2025-12-10 17:07:55.667 +04 / 2025-12-10 13:07:55.667 UTC (1765372075667)
  Pid: 13424
  Go Version: go1.24.9
  Python Version: unused
  Build arch: amd64
  Agent flavor: agent
  FIPS Mode: not available
  Log Level: info

  Paths
  =====
    Config File: C:\ProgramData\Datadog\datadog.yaml
    conf.d: C:\ProgramData\Datadog\conf.d
    checks.d: C:\ProgramData\Datadog\checks.d

========
Hostname
========

  hostname: Niraj
  hostname-resolution-version: 1
  socket-fqdn: Niraj
  socket-hostname: Niraj
  host tags:
    env:hackathon-dev
  hostname provider: os
  unused hostname providers:
    'hostname' configuration/environment: hostname is empty
    'hostname_file' configuration/environment: 'hostname_file' configuration is not enabled
    aws: not retrieving hostname from AWS: the host is not an ECS instance and other providers already retrieve non-default hostnames
    azure: azure_hostname_style is set to 'os'
    container: the agent is not containerized
    fargate: agent is not running in sidecar mode
    fqdn: 'hostname_fqdn' configuration is not enabled
    gce: unable to retrieve hostname from GCE: GCE metadata API error: Get "http://169.254.169.254/computeMetadata/v1/instance/hostname": dial tcp 169.254.169.254:80: connectex: A socket operation was attempted to an unreachable network.


Host Info
=========
  bootTime: 2025-12-09 11:54:51 +04 / 2025-12-09 07:54:51 UTC (1765266891000)
  kernelArch: amd64
  os: windows
  platform: Windows 11 Pro
  platformFamily: Windows 11 Pro
  platformVersion: 10.0 Build 26100
  procs: 367
  uptime: 29h13m3s


======
Clocks
======

NTP offset: 50.632ms

=================
HA Agent Metadata
=================


========
Metadata
========

  agent_startup_time_ms: 1765372075667
  agent_version: 7.73.0
  application_monitoring_config: []
  application_monitoring_config_fleet: []
  auto_instrumentation_modes: []
  config_apm_dd_url:
  config_dd_url:
  config_eks_fargate: false
  config_id:
  config_logs_dd_url:
  config_logs_socks5_proxy_address:
  config_no_proxy: [169.254.169.254 100.100.100.200]
  config_process_dd_url:
  config_proxy_http:
  config_proxy_https:
  config_site: us5.datadoghq.com
  diagnostics: map[connectivity:[{success Agent installation  map[endpoint:https://install.datadoghq.com]} {success Agent package yum  map[endpoint:https://yum.datadoghq.com]} {success Agent package apt  map[endpoint:https://apt.datadoghq.com]} {success Agent keys  map[endpoint:https://keys.datadoghq.com]} {success APM traces  map[endpoint:https://trace.agent.us5.datadoghq.com./_health]} {success Remote configuration  map[endpoint:https://config.us5.datadoghq.com./_health]} {failure LLM obs invalid status code map[endpoint:https://llmobs-intake.us5.datadoghq.com./api/v2/llmobs raw_error:invalid status code: 403]} {failure Connectivity to https://dbm-metrics-intake.us5.datadoghq.com./api/v2/databasequery Connection to `https://dbm-metrics-intake.us5.datadoghq.com./api/v2/databasequery` failed map[remediation:Please validate Agent configuration and firewall to access https://dbm-metrics-intake.us5.datadoghq.com./api/v2/databasequery]} {failure Connectivity to https://dbm-metrics-intake.us5.datadoghq.com./api/v2/dbmmetrics Connection to `https://dbm-metrics-intake.us5.datadoghq.com./api/v2/dbmmetrics` failed map[remediation:Please validate Agent configuration and firewall to access https://dbm-metrics-intake.us5.datadoghq.com./api/v2/dbmmetrics]} {failure Connectivity to https://dbm-metrics-intake.us5.datadoghq.com./api/v2/dbmmetadata Connection to `https://dbm-metrics-intake.us5.datadoghq.com./api/v2/dbmmetadata` failed map[remediation:Please validate Agent configuration and firewall to access https://dbm-metrics-intake.us5.datadoghq.com./api/v2/dbmmetadata]} {failure Connectivity to https://dbm-metrics-intake.us5.datadoghq.com./api/v2/dbmactivity Connection to `https://dbm-metrics-intake.us5.datadoghq.com./api/v2/dbmactivity` failed map[remediation:Please validate Agent configuration and firewall to access https://dbm-metrics-intake.us5.datadoghq.com./api/v2/dbmactivity]} {failure Connectivity to https://dbm-metrics-intake.us5.datadoghq.com./api/v2/dbmhealth Connection to `https://dbm-metrics-intake.us5.datadoghq.com./api/v2/dbmhealth` failed map[remediation:Please validate Agent configuration and firewall to access https://dbm-metrics-intake.us5.datadoghq.com./api/v2/dbmhealth]} {failure Connectivity to https://ndm-intake.us5.datadoghq.com./api/v2/ndm Connection to `https://ndm-intake.us5.datadoghq.com./api/v2/ndm` failed map[remediation:Please validate Agent configuration and firewall to access https://ndm-intake.us5.datadoghq.com./api/v2/ndm]} {failure Connectivity to https://snmp-traps-intake.us5.datadoghq.com./api/v2/ndmtraps Connection to `https://snmp-traps-intake.us5.datadoghq.com./api/v2/ndmtraps` failed map[remediation:Please validate Agent configuration and firewall to access https://snmp-traps-intake.us5.datadoghq.com./api/v2/ndmtraps]} {failure Connectivity to https://ndmflow-intake.us5.datadoghq.com./api/v2/ndmflow Connection to `https://ndmflow-intake.us5.datadoghq.com./api/v2/ndmflow` failed map[remediation:Please validate Agent configuration and firewall to access https://ndmflow-intake.us5.datadoghq.com./api/v2/ndmflow]} {failure Connectivity to https://netpath-intake.us5.datadoghq.com./api/v2/netpath Connection to `https://netpath-intake.us5.datadoghq.com./api/v2/netpath` failed map[remediation:Please validate Agent configuration and firewall to access https://netpath-intake.us5.datadoghq.com./api/v2/netpath]} {failure Connectivity to https://contlcycle-intake.us5.datadoghq.com./api/v2/contlcycle Connection to `https://contlcycle-intake.us5.datadoghq.com./api/v2/contlcycle` failed map[remediation:Please validate Agent configuration and firewall to access https://contlcycle-intake.us5.datadoghq.com./api/v2/contlcycle]} {failure Connectivity to https://contimage-intake.us5.datadoghq.com./api/v2/contimage Connection to `https://contimage-intake.us5.datadoghq.com./api/v2/contimage` failed map[remediation:Please validate Agent configuration and firewall to access https://contimage-intake.us5.datadoghq.com./api/v2/contimage]} {failure Connectivity to https://sbom-intake.us5.datadoghq.com./api/v2/sbom Connection to `https://sbom-intake.us5.datadoghq.com./api/v2/sbom` failed map[remediation:Please validate Agent configuration and firewall to access https://sbom-intake.us5.datadoghq.com./api/v2/sbom]} {failure Connectivity to https://http-synthetics.us5.datadoghq.com./api/v2/synthetics Connection to `https://http-synthetics.us5.datadoghq.com./api/v2/synthetics` failed map[remediation:Please validate Agent configuration and firewall to access https://http-synthetics.us5.datadoghq.com./api/v2/synthetics]} {success Connectivity to https://app.us5.datadoghq.com./api/v1/series  map[]} {success Connectivity to https://app.us5.datadoghq.com./api/v1/check_run  map[]} {success Connectivity to https://app.us5.datadoghq.com./intake/  map[]} {failure Connectivity to https://app.us5.datadoghq.com./api/v1/validate
...Retrieving or creating a new connection
...Reusing a previous connection that was idle for 4.6163ms
Connection to `https://app.us5.datadoghq.com./api/v1/validate` failed
Received response : '{"err... map[remediation:Please validate Agent configuration and firewall to access https://app.us5.datadoghq.com./api/v1/validate]} {success Connectivity to https://app.us5.datadoghq.com./api/v1/metadata  map[]} {success Connectivity to https://app.us5.datadoghq.com./api/v2/series  map[]} {success Connectivity to https://app.us5.datadoghq.com./api/beta/sketches  map[]} {success Connectivity to https://7-73-0-flare.agent.us5.datadoghq.com./support/flare  map[]}]]
  feature_apm_enabled: true
  feature_auto_instrumentation_enabled: false
  feature_container_images_enabled: true
  feature_csm_vm_containers_enabled: false
  feature_csm_vm_hosts_enabled: false
  feature_cspm_enabled: false
  feature_cspm_host_benchmarks_enabled: false
  feature_cws_enabled: false
  feature_cws_network_enabled: true
  feature_cws_remote_config_enabled: true
  feature_cws_security_profiles_enabled: false
  feature_discovery_enabled: false
  feature_dynamic_instrumentation_enabled: false
  feature_gpu_monitoring_enabled: false
  feature_imdsv2_enabled: false
  feature_logs_enabled: false
  feature_networks_enabled: false
  feature_networks_http_enabled: true
  feature_networks_https_enabled: true
  feature_oom_kill_enabled: false
  feature_otlp_enabled: false
  feature_process_enabled: false
  feature_process_language_detection_enabled: false
  feature_processes_container_enabled: true
  feature_remote_configuration_enabled: true
  feature_synthetics_collector_enabled: false
  feature_tcp_queue_length_enabled: false
  feature_traceroute_enabled: false
  feature_usm_enabled: false
  feature_usm_go_tls_enabled: true
  feature_usm_http2_enabled: false
  feature_usm_istio_enabled: true
  feature_usm_kafka_enabled: false
  feature_usm_postgres_enabled: false
  feature_usm_redis_enabled: false
  feature_windows_crash_detection_enabled: false
  fips_mode: false
  flavor: agent
  fleet_policies_applied: []
  hostname_source: os
  infrastructure_mode: full
  install_method_installer_version: install-script-default_package
  install_method_tool: installer
  install_method_tool_version: 7.73.0
  system_probe_core_enabled: true
  system_probe_gateway_lookup_enabled: true
  system_probe_kernel_headers_download_enabled: false
  system_probe_max_connections_per_message: 600
  system_probe_prebuilt_fallback_enabled: false
  system_probe_protocol_classification_enabled: true
  system_probe_root_namespace_enabled: true
  system_probe_runtime_compilation_enabled: false
  system_probe_telemetry_enabled: false
  system_probe_track_tcp_4_connections: true
  system_probe_track_tcp_6_connections: true
  system_probe_track_udp_4_connections: true
  system_probe_track_udp_6_connections: true

=========
Collector
=========


  Running Checks
  ==============

    agentcrashdetect
    ----------------
      Instance ID: agentcrashdetect [OK]
      Configuration Source: file:C:\ProgramData\Datadog\conf.d\agentcrashdetect.d\conf.yaml.default[0]
      Total Runs: 7,998
      Metric Samples: Last Run: 0, Total: 0
      Events: Last Run: 0, Total: 0
      Service Checks: Last Run: 0, Total: 0
      Average Execution Time : 0s
      Last Execution Date : 2025-12-17 10:06:32.353 +04 / 2025-12-17 06:06:32.353 UTC (1765951592353)
      Last Successful Execution Date : 2025-12-17 10:06:32 +04 / 2025-12-17 06:06:32 UTC (1765951592000)
      metadata:
        config.source: C:\ProgramData\Datadog\conf.d\agentcrashdetect.d\conf.yaml.default[0]


    container_image
    ---------------
      Instance ID: container_image [OK]
      Long Running Check: true
      Configuration Source: file:C:\ProgramData\Datadog\conf.d\container_image.d\conf.yaml.default[0]
      Total Metric Samples: 0
      Total Events: 0
      Total Service Checks: 0
      metadata:
        config.source: C:\ProgramData\Datadog\conf.d\container_image.d\conf.yaml.default[0]


    container_lifecycle
    -------------------
      Instance ID: container_lifecycle [OK]
      Long Running Check: true
      Configuration Source: file:C:\ProgramData\Datadog\conf.d\container_lifecycle.d\conf.yaml.default[0]
      Total Metric Samples: 0
      Total Events: 0
      Total Service Checks: 0
      metadata:
        config.source: C:\ProgramData\Datadog\conf.d\container_lifecycle.d\conf.yaml.default[0]


    cpu
    ---
      Instance ID: cpu [OK]
      Configuration Source: file:C:\ProgramData\Datadog\conf.d\cpu.d\conf.yaml.default[0]
      Total Runs: 7,997
      Metric Samples: Last Run: 8, Total: 63,976
      Events: Last Run: 0, Total: 0
      Service Checks: Last Run: 0, Total: 0
      Average Execution Time : 0s
      Last Execution Date : 2025-12-17 10:06:23.355 +04 / 2025-12-17 06:06:23.355 UTC (1765951583355)
      Last Successful Execution Date : 2025-12-17 10:06:23 +04 / 2025-12-17 06:06:23 UTC (1765951583000)
      metadata:
        config.source: C:\ProgramData\Datadog\conf.d\cpu.d\conf.yaml.default[0]


    disk
    ----
      Instance ID: disk [OK]
      Configuration Source: file:C:\ProgramData\Datadog\conf.d\disk.d\conf.yaml.default[0]
      Total Runs: 7,997
      Metric Samples: Last Run: 9, Total: 71,973
      Events: Last Run: 0, Total: 0
      Service Checks: Last Run: 0, Total: 0
      Average Execution Time : 0s
      Last Execution Date : 2025-12-17 10:06:30.355 +04 / 2025-12-17 06:06:30.355 UTC (1765951590355)
      Last Successful Execution Date : 2025-12-17 10:06:30 +04 / 2025-12-17 06:06:30 UTC (1765951590000)
      metadata:
        config.source: C:\ProgramData\Datadog\conf.d\disk.d\conf.yaml.default[0]


    file_handle
    -----------
      Instance ID: file_handle [OK]
      Configuration Source: file:C:\ProgramData\Datadog\conf.d\file_handle.d\conf.yaml.default[0]
      Total Runs: 7,997
      Metric Samples: Last Run: 1, Total: 7,997
      Events: Last Run: 0, Total: 0
      Service Checks: Last Run: 0, Total: 0
      Average Execution Time : 21ms
      Last Execution Date : 2025-12-17 10:06:22.369 +04 / 2025-12-17 06:06:22.369 UTC (1765951582369)
      Last Successful Execution Date : 2025-12-17 10:06:22 +04 / 2025-12-17 06:06:22 UTC (1765951582000)
      metadata:
        config.source: C:\ProgramData\Datadog\conf.d\file_handle.d\conf.yaml.default[0]


    io
    --
      Instance ID: io [OK]
      Configuration Source: file:C:\ProgramData\Datadog\conf.d\io.d\conf.yaml.default[0]
      Total Runs: 7,997
      Metric Samples: Last Run: 14, Total: 111,958
      Events: Last Run: 0, Total: 0
      Service Checks: Last Run: 0, Total: 0
      Average Execution Time : 0s
      Last Execution Date : 2025-12-17 10:06:29.354 +04 / 2025-12-17 06:06:29.354 UTC (1765951589354)
      Last Successful Execution Date : 2025-12-17 10:06:29 +04 / 2025-12-17 06:06:29 UTC (1765951589000)
      metadata:
        config.source: C:\ProgramData\Datadog\conf.d\io.d\conf.yaml.default[0]


    memory
    ------
      Instance ID: memory [OK]
      Configuration Source: file:C:\ProgramData\Datadog\conf.d\memory.d\conf.yaml.default[0]
      Total Runs: 7,998
      Metric Samples: Last Run: 17, Total: 135,966
      Events: Last Run: 0, Total: 0
      Service Checks: Last Run: 0, Total: 0
      Average Execution Time : 1ms
      Last Execution Date : 2025-12-17 10:06:36.354 +04 / 2025-12-17 06:06:36.354 UTC (1765951596354)
      Last Successful Execution Date : 2025-12-17 10:06:36 +04 / 2025-12-17 06:06:36 UTC (1765951596000)
      metadata:
        config.source: C:\ProgramData\Datadog\conf.d\memory.d\conf.yaml.default[0]


    network
    -------
      Instance ID: network [OK]
      Configuration Source: file:C:\ProgramData\Datadog\conf.d\network.d\conf.yaml.default[0]
      Total Runs: 7,997
      Metric Samples: Last Run: 105, Total: 839,685
      Events: Last Run: 0, Total: 0
      Service Checks: Last Run: 0, Total: 0
      Average Execution Time : 31ms
      Last Execution Date : 2025-12-17 10:06:28.387 +04 / 2025-12-17 06:06:28.387 UTC (1765951588387)
      Last Successful Execution Date : 2025-12-17 10:06:28 +04 / 2025-12-17 06:06:28 UTC (1765951588000)
      metadata:
        config.source: C:\ProgramData\Datadog\conf.d\network.d\conf.yaml.default[0]


    ntp
    ---
      Instance ID: ntp:3c427a42a70bbf8 [OK]
      Configuration Source: file:C:\ProgramData\Datadog\conf.d\ntp.d\conf.yaml.default[0]
      Total Runs: 134
      Metric Samples: Last Run: 1, Total: 134
      Events: Last Run: 0, Total: 0
      Service Checks: Last Run: 1, Total: 134
      Average Execution Time : 464ms
      Last Execution Date : 2025-12-17 10:02:19.185 +04 / 2025-12-17 06:02:19.185 UTC (1765951339185)
      Last Successful Execution Date : 2025-12-17 10:02:19 +04 / 2025-12-17 06:02:19 UTC (1765951339000)
      metadata:
        config.source: C:\ProgramData\Datadog\conf.d\ntp.d\conf.yaml.default[0]


    telemetry
    ---------
      Instance ID: telemetry [OK]
      Configuration Source: file:C:\ProgramData\Datadog\conf.d\telemetry.d\conf.yaml.default[0]
      Total Runs: 7,998
      Metric Samples: Last Run: 9, Total: 64,474
      Events: Last Run: 0, Total: 0
      Service Checks: Last Run: 0, Total: 0
      Average Execution Time : 0s
      Last Execution Date : 2025-12-17 10:06:35.353 +04 / 2025-12-17 06:06:35.353 UTC (1765951595353)
      Last Successful Execution Date : 2025-12-17 10:06:35 +04 / 2025-12-17 06:06:35 UTC (1765951595000)
      metadata:
        config.source: C:\ProgramData\Datadog\conf.d\telemetry.d\conf.yaml.default[0]


    uptime
    ------
      Instance ID: uptime [OK]
      Configuration Source: file:C:\ProgramData\Datadog\conf.d\uptime.d\conf.yaml.default[0]
      Total Runs: 7,997
      Metric Samples: Last Run: 1, Total: 7,997
      Events: Last Run: 0, Total: 0
      Service Checks: Last Run: 0, Total: 0
      Average Execution Time : 0s
      Last Execution Date : 2025-12-17 10:06:27.354 +04 / 2025-12-17 06:06:27.354 UTC (1765951587354)
      Last Successful Execution Date : 2025-12-17 10:06:27 +04 / 2025-12-17 06:06:27 UTC (1765951587000)
      metadata:
        config.source: C:\ProgramData\Datadog\conf.d\uptime.d\conf.yaml.default[0]


    winproc
    -------
      Instance ID: winproc [OK]
      Configuration Source: file:C:\ProgramData\Datadog\conf.d\winproc.d\conf.yaml.default[0]
      Total Runs: 7,998
      Metric Samples: Last Run: 2, Total: 15,996
      Events: Last Run: 0, Total: 0
      Service Checks: Last Run: 0, Total: 0
      Average Execution Time : 20ms
      Last Execution Date : 2025-12-17 10:06:34.376 +04 / 2025-12-17 06:06:34.376 UTC (1765951594376)
      Last Successful Execution Date : 2025-12-17 10:06:34 +04 / 2025-12-17 06:06:34 UTC (1765951594000)
      metadata:
        config.source: C:\ProgramData\Datadog\conf.d\winproc.d\conf.yaml.default[0]

  Check Worker Utilization
  ========================
    Total Workers: 4

    Top Workers (by utilization):
      worker_1: 0.0%
      worker_2: 0.0%
      worker_3: 0.0%
      worker_4: 0.0%

==========
Aggregator
==========

  Checks Metric Sample: 1,558,510
  Dogstatsd Metric Sample: 1,958,161
  Event: 1
  Events Flushed: 1
  Number Of Flushes: 8,036
  Series Flushed: 2,333,159
  Service Check: 134
  Service Checks Flushed: 8,170

=========
APM Agent
=========

  Status: Running
  Pid: 3544
  Uptime: 579521 seconds
  Mem alloc: 15,497,512 bytes
  Hostname: Niraj
  Receiver: localhost:8126
  Endpoints:
    https://trace.agent.us5.datadoghq.com.

  Receiver (previous minute)
  ==========================
    No traces received in the previous minute.



  Writer (previous minute)
  ========================
    Traces: 0 payloads, 0 traces, 0 events, 0 bytes
    Stats: 0 payloads, 0 stats buckets, 0 bytes

=========
DogStatsD
=========

  Event Packets: 0
  Event Parse Errors: 0
  Metric Packets: 1,958,160
  Metric Parse Errors: 0
  Service Check Packets: 0
  Service Check Parse Errors: 0
  Udp Bytes: 205,712,669
  Udp Packet Reading Errors: 0
  Udp Packets: 617,865
  Uds Bytes: 0
  Uds Origin Detection Errors: 0
  Uds Packet Reading Errors: 0
  Uds Packets: 0
  Unterminated Metric Errors: 0

Tip: For troubleshooting, enable 'dogstatsd_metrics_stats_enable' in the main datadog.yaml file to generate Dogstatsd logs. Once 'dogstatsd_metrics_stats_enable' is enabled, users can also use 'dogstatsd-stats' command to get visibility of the latest collected metrics.

=========
Endpoints
=========

  https://app.us5.datadoghq.com. - API Key ending with:
      - 97915

================
Fleet Automation
================


  Fleet Management is enabled

  Remote Management Status:    Enabled
  Datadog Installer Status:    Running


=========
Forwarder
=========

  Transactions
  ============
    Cluster: 0
    ClusterRole: 0
    ClusterRoleBinding: 0
    CronJob: 0
    CustomResource: 0
    CustomResourceDefinition: 0
    DaemonSet: 0
    Deployment: 0
    Dropped: 0
    ECSTask: 0
    EndpointSlice: 0
    HighPriorityQueueFull: 0
    HorizontalPodAutoscaler: 0
    Ingress: 0
    Job: 0
    KubeletConfiguration: 0
    LimitRange: 0
    Namespace: 0
    NetworkPolicy: 0
    Node: 0
    OrchestratorManifest: 0
    PersistentVolume: 0
    PersistentVolumeClaim: 0
    Pod: 0
    PodDisruptionBudget: 0
    ReplicaSet: 0
    Requeued: 743
    Retried: 243
    RetryQueueSize: 0
    Role: 0
    RoleBinding: 0
    Service: 0
    ServiceAccount: 0
    StatefulSet: 0
    StorageClass: 0
    VerticalPodAutoscaler: 0

  Transaction Successes
  =====================
    Total number: 18050
    Successes By Endpoint:
      check_run_v1: 8,036
      intake: 321
      metadata_v1: 1,657
      series_v2: 8,036

  Transaction Errors
  ==================
    Total number: 139
    Errors By Type:
      ConnectionErrors: 3
      DNSErrors: 6

  On-disk storage
  ===============
    On-disk storage is disabled. Configure `forwarder_storage_max_size_in_bytes` to enable it.

  API Keys errors
  ===============
    API key ending with 97915: API Key invalid

=========
JMX Fetch
=========

  Information
  ==================
  Initialized checks
  ==================
    no checks

  Failed checks
  =============
    no checks


==========
Logs Agent
==========

  Logs Agent is not running

==========
OTel Agent
==========


  Status: Not running or unreachable on https://localhost:7777.
  Error: OTel Agent is not enabled.

====
OTLP
====

  Status: Not enabled
  Collector status: Not running



=============
Process Agent
=============

  Version: 7.73.0
  Status date: 2025-12-17 10:06:36.78 +04 / 2025-12-17 06:06:36.78 UTC (1765951596780)
  Process Agent Start: 2025-12-10 17:07:56.908 +04 / 2025-12-10 13:07:56.908 UTC (1765372076908)
  Pid: 4800
  Go Version: go1.24.9
  Build arch: amd64
  Log Level: info
  Enabled Checks: [process_discovery rtcontainer container]
  Allocated Memory: 0 bytes
  Hostname: Niraj
  System Probe Process Module Status: Not running
  Process Language Detection Enabled: False

  =================
  Process Endpoints
  =================
    https://process.us5.datadoghq.com. - API Key ending with:
        - 97915

  =========
  Collector
  =========
    Last collection time: 2025-12-17 10:06:27
    Docker socket:
    Number of processes: 0
    Number of containers: 0
    Process Queue length: 0
    RTProcess Queue length: 0
    Connections Queue length: 0
    Event Queue length: 0
    Pod Queue length: 0
    Process Bytes enqueued: 0
    RTProcess Bytes enqueued: 0
    Connections Bytes enqueued: 0
    Event Bytes enqueued: 0
    Pod Bytes enqueued: 0
    Drop Check Payloads: []
    Number of submission errors: 15

  ==========
  Extractors
  ==========

    Workloadmeta
    ============
      Cache size: 0
      Stale diffs discarded: 0
      Diffs dropped: 0

=============
Remote Agents
=============

No remote agents registered

====================
Remote Configuration
====================


Organization enabled: True
API Key: Authorized
Last error: non-200 response code: 401



=======
Secrets
=======

No secret_backend_command set: secrets feature is not enabled
===
SSI
===

    SSI is not enabled.


========================
Transport Proxy Warnings
========================

  No Transport Proxy Warnings
