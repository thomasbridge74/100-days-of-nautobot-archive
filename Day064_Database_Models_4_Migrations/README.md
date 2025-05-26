# Nautobot Database Model Part 4: Migrations 

We have been using the `makemigrations` and `migrate` commands to propagate changes we made to the data models into the database. 

Django's migration framework is designed to be flexible and powerful, allowing use to evolve our database schema over time without losing data.

In today's challenge, we will discuss database migration. 

## Environment Setup

We will use a combination of [Scenario 2](../Lab_Setup/scenario_2_setup/README.md) lab, [https://demo.nautobot.com/](https://demo.nautobot.com/), and [Nautobot Documentation](https://docs.nautobot.com/projects/core/en/latest/user-guide/core-data-model/overview/introduction/) for today's challenge. 

```
$ cd nautobot
$ poetry shell
$ poetry install
$ invoke build
(be patient with this step)
$ invoke debug
(be patient with this step as well)
```

## Migration Rollback

We do not need to do this often (so we hope), but if needed, we can choose to migrate back to an older database schema. 

Let's begin by looking at the migration history, notice all the changes the record all the way back to the initial migration and separated by tables: 

> [!INFORMATION]
> Your output might look different. 

```shell 
(nautobot-py3.10) @ericchou1 ➜ ~/nautobot (develop) $ docker exec -it nautobot-2-4-nautobot-1 bash

root@c8032ee34216:/source# nautobot-server showmigrations
admin
 [X] 0001_initial
 [X] 0002_logentry_remove_auto_add
 [X] 0003_logentry_add_action_flag_choices
auth
 [X] 0001_initial
 [X] 0002_alter_permission_name_max_length
 [X] 0003_alter_user_email_max_length
 [X] 0004_alter_user_username_opts
 [X] 0005_alter_user_last_login_null
 [X] 0006_require_contenttypes_0002
 [X] 0007_alter_validators_add_error_messages
 [X] 0008_alter_user_username_max_length
 [X] 0009_alter_user_last_name_max_length
 [X] 0010_alter_group_name_max_length
 [X] 0011_update_proxy_permissions
 [X] 0012_alter_user_first_name_max_length
circuits
 [X] 0001_initial_part_1
 [X] 0002_initial_part_2
 [X] 0003_auto_slug
 [X] 0004_increase_provider_account_length
 [X] 0005_providernetwork
 [X] 0006_cache_circuit_terminations
 [X] 0007_circuitterminations_primary_model
 [X] 0008_add_natural_indexing
 [X] 0009_circuittermination_location
 [X] 0010_rename_foreign_keys_and_related_names
 [X] 0011_remove_site_foreign_key_from_circuit_termination_class
 [X] 0012_created_datetime
 [X] 0013_alter_circuittermination__path
 [X] 0014_related_name_changes
 [X] 0015_remove_circuittype_provider_slug
 [X] 0016_tagsfield
 [X] 0017_fixup_null_statuses
 [X] 0018_status_nonnullable
 [X] 0019_remove_providernetwork_slug
 [X] 0020_update_all_charfields_max_length_to_255
 [X] 0021_alter_circuit_status_alter_circuittermination__path
 [X] 0022_circuittermination_cloud_network
cloud
 [X] 0001_initial
constance
 [X] 0001_initial
 [X] 0002_migrate_from_old_table
 [X] 0003_drop_pickle
contenttypes
 [X] 0001_initial
 [X] 0002_remove_content_type_name
dcim
 [X] 0001_initial_part_1
 [X] 0002_initial_part_2
 [X] 0003_initial_part_3
 [X] 0004_initial_part_4
 [X] 0005_device_local_context_schema
 [X] 0006_auto_slug
 [X] 0007_device_secrets_group
 [X] 0008_increase_all_serial_lengths
 [X] 0009_add_natural_indexing
 [X] 0010_interface_status
 [X] 0011_interface_status_data_migration
 [X] 0012_interface_parent_bridge
 [X] 0013_location_location_type
 [X] 0014_location_status_data_migration
 [X] 0015_device_components__changeloggedmodel
 [X] 0016_device_components__timestamp_data_migration
 [X] 0017_locationtype_nestable
 [X] 0018_device_redundancy_group
 [X] 0019_device_redundancy_group_data_migration
 [X] 0020_increase_device_asset_tag_size_limit
 [X] 0021_platform_network_driver
 [X] 0022_interface_redundancy_group
 [X] 0023_interface_redundancy_group_data_migration
 [X] 0024_move_site_fields_to_location_model
 [X] 0025_mptt_to_tree_queries
 [X] 0026_interface_mac_address_data_migration
 [X] 0027_alter_interface_mac_address
 [X] 0028_alter_device_and_rack_role_add_new_role
 [X] 0029_device_and_rack_roles_data_migrations
 [X] 0030_rename_device_and_rack_role
 [X] 0031_remove_device_role_and_rack_role
 [X] 0032_rename_foreignkey_fields
 [X] 0033_add_tree_managers_and_foreign_keys_pre_data_migration
 [X] 0034_migrate_region_and_site_data_to_locations
 [X] 0035_rename_path_end_point_related_name
 [X] 0036_remove_site_foreign_key_from_dcim_models
 [X] 0037_created_datetime
 [X] 0038_fixup_fks_and_related_names
 [X] 0039_related_name_changes
 [X] 0040_remove_region_and_site
 [X] 0041_interface_ip_addresses_m2m
 [X] 0042_alter_location_managers
 [X] 0043_remove_slug
 [X] 0044_tagsfield
 [X] 0045_ipam__namespaces
 [X] 0046_fixup_null_statuses
 [X] 0047_status_nonnullable
 [X] 0048_ensure_virtual_chassis_names_are_unique_and_add_uniqueness_constraint
 [X] 0049_remove_slugs_and_change_device_primary_ip_fields
 [X] 0050_fix_interface_redundancy_group_association_created
 [X] 0051_interface_redundancy_group_nullable_status
 [X] 0052_fix_interface_redundancy_group_created
 [X] 0053_create_device_family_model
 [X] 0054_softwareimage_softwareversion
 [X] 0055_softwareimage_softwareversion_data_migration
 [X] 0056_update_all_charfields_max_length_to_255
 [X] 0057_controller_models
 [X] 0058_controller_data_migration
 [X] 0059_add_role_field_to_interface_models
 [X] 0060_alter_cable_status_alter_consoleport__path_and_more
 [X] 0061_module_models
 [X] 0062_module_data_migration
 [X] 0063_interfacevdcassignment_virtualdevicecontext_and_more
 [X] 0064_virtualdevicecontext_status_data_migration
 [X] 0065_controller_capabilities_and_more
 [X] 0066_controllermanageddevicegroup_radio_profiles_and_more
 [X] 0067_controllermanageddevicegroup_tenant
 [X] 0068_asset
 [X] 0069_maintenanceschedule
django_celery_beat
 [X] 0001_initial
 [X] 0002_auto_20161118_0346
 [X] 0003_auto_20161209_0049
 [X] 0004_auto_20170221_0000
 [X] 0005_add_solarschedule_events_choices
 [X] 0006_auto_20180322_0932
 [X] 0007_auto_20180521_0826
 [X] 0008_auto_20180914_1922
 [X] 0006_auto_20180210_1226
 [X] 0006_periodictask_priority
 [X] 0009_periodictask_headers
 [X] 0010_auto_20190429_0326
 [X] 0011_auto_20190508_0153
 [X] 0012_periodictask_expire_seconds
 [X] 0013_auto_20200609_0727
 [X] 0014_remove_clockedschedule_enabled
 [X] 0015_edit_solarschedule_events_choices
 [X] 0016_alter_crontabschedule_timezone
 [X] 0017_alter_crontabschedule_month_of_year
 [X] 0018_improve_crontab_helptext
django_celery_results
 [X] 0001_initial
 [X] 0002_add_task_name_args_kwargs
 [X] 0003_auto_20181106_1101
 [X] 0004_auto_20190516_0412
 [X] 0005_taskresult_worker
 [X] 0006_taskresult_date_created
 [X] 0007_remove_taskresult_hidden
 [X] 0008_chordcounter
 [X] 0009_groupresult
 [X] 0010_remove_duplicate_indices
 [X] 0011_taskresult_periodic_task_name
example_app
 [X] 0001_initial
 [X] 0002_anotherexamplemodel
 [X] 0003_anotherexamplemodel__custom_field_data
 [X] 0004_example_models_dynamicgroup
 [X] 0005_created_datetime
 [X] 0006_add_natural_keys
 [X] 0007_update_all_charfields_max_length_to_255
 [X] 0008_usefullink
extras
 [X] 0001_initial_part_1
 [X] 0002_initial_part_2
 [X] 0003_initial_part_3
 [X] 0004_populate_default_status_records
 [X] 0005_configcontext_device_types
 [X] 0006_graphqlquery
 [X] 0007_configcontextschema
 [X] 0008_jobresult__custom_field_data
 [X] 0009_computedfield
 [X] 0010_change_cf_validation_max_min_field_to_bigint
 [X] 0011_fileattachment_fileproxy
 [X] 0012_healthchecktestmodel
 [X] 0013_default_fallback_value_computedfield
 [X] 0014_auto_slug
 [X] 0015_scheduled_job
 [X] 0016_secret
 [X] 0017_joblogentry
 [X] 0018_joblog_data_migration
 [X] 0019_joblogentry__meta_options__related_name
 [X] 0020_customfield_changelog
 [X] 0021_customfield_changelog_data
 [X] 0022_objectchange_object_datav2
 [X] 0023_job_model
 [X] 0024_job_data_migration
 [X] 0025_add_advanced_ui_boolean_to_customfield_conputedfield_and_relationship
 [X] 0026_job_add_gitrepository_fk
 [X] 0027_job_gitrepository_data_migration
 [X] 0028_job_reduce_source
 [X] 0029_dynamicgroup
 [X] 0030_webhook_alter_unique_together
 [X] 0031_tag_content_types
 [X] 0032_tag_content_types_data_migration
 [X] 0033_add__optimized_indexing
 [X] 0034_alter_fileattachment_mimetype
 [X] 0035_scheduledjob_crontab
 [X] 0036_job_add_has_sensitive_variables
 [X] 0037_configcontextschema__remove_name_unique__create_constraint_unique_name_owner
 [X] 0038_configcontext_locations
 [X] 0039_objectchange__add_change_context
 [X] 0040_dynamicgroup__dynamicgroupmembership
 [X] 0041_jobresult_job_kwargs
 [X] 0042_job__add_is_job_hook_receiver
 [X] 0043_note
 [X] 0044_add_job_hook
 [X] 0045_add_custom_field_slug
 [X] 0046_populate_custom_field_slug_label
 [X] 0047_enforce_custom_field_slug
 [X] 0048_alter_objectchange_change_context_detail
 [X] 0049_alter_tag_slug
 [X] 0050_customfield_grouping
 [X] 0051_add_job_task_queues
 [X] 0052_configcontext_device_redundancy_groups
 [X] 0053_relationship_required_on
 [X] 0054_scheduledjob_kwargs_request_user_change
 [X] 0055_configcontext_dynamic_groups
 [X] 0056_objectchange_add_reverse_time_idx
 [X] 0057_jobbutton
 [X] 0058_jobresult_add_time_status_idxs
 [X] 0059_joblogentry_scheduledjob_webhook_data_migration
 [X] 0060_alter_joblogentry_scheduledjob_webhook_fields
 [X] 0061_role_and_alter_status
 [X] 0062_collect_roles_from_related_apps_roles
 [X] 0063_alter_role_options
 [X] 0064_alter_configcontext_and_add_new_role
 [X] 0065_configcontext_data_migrations
 [X] 0066_rename_configcontext_role
 [X] 0067_migrate_job_result_status
 [X] 0068_jobresult__add_celery_fields
 [X] 0069_created_datetime
 [X] 0070_remove_site_and_region_attributes_from_config_context
 [X] 0071_replace_related_names
 [X] 0072_rename_model_fields
 [X] 0073_job__unique_name_data_migration
 [X] 0074_job__unique_name
 [X] 0075_remove_gitrepository_fields
 [X] 0076_rename_slug_to_key_for_custom_field
 [X] 0077_migrate_custom_field_data
 [X] 0078_remove_name_field_and_make_label_field_non_nullable
 [X] 0079_remove_slug
 [X] 0080_tagsfield
 [X] 0081_rename_relationship_slug_to_key
 [X] 0082_rename_relationship_name_to_label
 [X] 0083_ensure_relationship_keys_are_unique
 [X] 0084_rename_computed_field_slug_to_key
 [X] 0085_taggeditem_cleanup
 [X] 0086_taggeditem_uniqueness
 [X] 0087_job__celery_task_fields__dryrun_support
 [X] 0088_job__commit_default_data_migration
 [X] 0089_joblogentry__log_level_default
 [X] 0090_joblogentry__log_level_data_migration
 [X] 0091_scheduledjob__data_migration
 [X] 0092_uniqueness_data_migration
 [X] 0093_uniqueness_fixup
 [X] 0094_alter_objectchange_unique_together
 [X] 0095_ensure_note_timestamps_are_unique
 [X] 0096_remove_slugs
 [X] 0097_alter_job_result_remove_result
 [X] 0098_rename_data_jobresult_result
 [X] 0099_remove_dangling_note_objects
 [X] 0100_fileproxy_job_result
 [X] 0101_externalintegration
 [X] 0102_set_null_objectchange_contenttype
 [X] 0103_add_db_indexes_to_object_change
 [X] 0104_contact_contactassociation_team
 [X] 0105_update_all_charfields_max_length_to_255
 [X] 0106_populate_default_statuses_and_roles_for_contact_associations
 [X] 0107_laxurlfield
 [X] 0108_jobbutton_enabled
 [X] 0109_dynamicgroup_group_type_dynamicgroup_tags_and_more
 [X] 0110_alter_configcontext_cluster_groups_and_more
 [X] 0111_metadata
 [X] 0112_dynamic_group_group_type_data_migration
 [X] 0113_saved_views
 [X] 0114_computedfield_grouping
 [X] 0115_scheduledjob_time_zone
 [X] 0116_fix_dynamic_group_group_type_data_migration
 [X] 0117_create_job_queue_model
 [X] 0118_task_queue_to_job_queue_migration
 [X] 0119_remove_task_queues_from_job_and_queue_from_scheduled_job
 [X] 0120_job_is_singleton_job_is_singleton_override
 [X] 0121_alter_team_contacts
 [X] 0122_add_graphqlquery_owner_content_type
ipam
 [X] 0001_initial_part_1
 [X] 0002_initial_part_2
 [X] 0003_remove_max_length
 [X] 0004_fixup_p2p_broadcast
 [X] 0005_auto_slug
 [X] 0006_ipaddress_nat_outside_list
 [X] 0007_add_natural_indexing
 [X] 0008_prefix_vlan_vlangroup_location
 [X] 0009_alter_vlan_name
 [X] 0010_alter_ipam_role_add_new_role
 [X] 0011_migrate_ipam_role_data
 [X] 0012_rename_ipam_roles
 [X] 0013_delete_role
 [X] 0014_rename_foreign_keys_and_related_names
 [X] 0015_prefix_add_type
 [X] 0016_prefix_type_data_migration
 [X] 0017_prefix_remove_is_pool
 [X] 0018_remove_site_foreign_key_from_ipam_models
 [X] 0019_created_datetime
 [X] 0020_related_name_changes
 [X] 0021_prefix_add_rir_and_date_allocated
 [X] 0022_aggregate_to_prefix_data_migration
 [X] 0023_delete_aggregate
 [X] 0024_interface_to_ipaddress_m2m
 [X] 0025_interface_ipaddress_m2m_data_migration
 [X] 0026_ipaddress_remove_assigned_object
 [X] 0027_remove_rir_slug
 [X] 0028_tagsfield
 [X] 0029_ip_address_to_interface_uniqueness_constraints
 [X] 0030_ipam__namespaces
 [X] 0031_ipam___data_migrations
 [X] 0032_ipam__namespaces_finish
 [X] 0033_fixup_null_statuses
 [X] 0034_status_nonnullable
 [X] 0035_ensure_all_services_fit_uniqueness_constraint
 [X] 0036_add_uniqueness_constraints_to_service
 [X] 0037_data_migration_vlan_group_name_uniqueness
 [X] 0038_vlan_group_name_unique_remove_slug
 [X] 0039_alter_ipaddresstointerface_ip_address
 [X] 0040_vlan_prefix_locations
 [X] 0041_vlan_prefix_locations_data_migration
 [X] 0042_remove_location_from_vlan_and_prefix
 [X] 0043_fixup_null_ip_version
 [X] 0044_ip_version_nonnullable
 [X] 0045_alter_vlangroup_options
 [X] 0046_update_all_charfields_max_length_to_255
 [X] 0047_alter_ipaddress_role_alter_ipaddress_status_and_more
 [X] 0048_vrf_status
 [X] 0049_vrf_data_migration
 [X] 0050_vlangroup_range
 [X] 0051_added_optional_vrf_relationship_to_vdc
sessions
 [X] 0001_initial
silk
 [X] 0001_initial
 [X] 0002_auto_update_uuid4_id_field
 [X] 0003_request_prof_file
 [X] 0004_request_prof_file_storage
 [X] 0005_increase_request_prof_file_length
 [X] 0006_fix_request_prof_file_blank
 [X] 0007_sqlquery_identifier
 [X] 0008_sqlquery_analysis
social_django
 [X] 0001_initial (2 squashed migrations)
 [X] 0002_add_related_name (2 squashed migrations)
 [X] 0003_alter_email_max_length (2 squashed migrations)
 [X] 0004_auto_20160423_0400 (2 squashed migrations)
 [X] 0005_auto_20160727_2333 (1 squashed migrations)
 [X] 0006_partial
 [X] 0007_code_timestamp
 [X] 0008_partial_timestamp
 [X] 0009_auto_20191118_0520
 [X] 0010_uid_db_index
 [X] 0011_alter_id_fields
 [X] 0012_usersocialauth_extra_data_new
 [X] 0013_migrate_extra_data
 [X] 0014_remove_usersocialauth_extra_data
 [X] 0015_rename_extra_data_new_usersocialauth_extra_data
 [X] 0016_alter_usersocialauth_extra_data
taggit
 [X] 0001_initial
 [X] 0002_auto_20150616_2121
 [X] 0003_taggeditem_add_unique_index
 [X] 0004_alter_taggeditem_content_type_alter_taggeditem_tag
 [X] 0005_auto_20220424_2025
 [X] 0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx
tenancy
 [X] 0001_initial
 [X] 0002_auto_slug
 [X] 0003_mptt_to_tree_queries
 [X] 0004_change_tree_manager_on_tree_models
 [X] 0005_rename_foreign_keys_and_related_names
 [X] 0006_created_datetime
 [X] 0007_remove_tenant_tenantgroup_slug
 [X] 0008_tagsfield
 [X] 0009_update_all_charfields_max_length_to_255
users
 [X] 0001_initial
 [X] 0002_token_ordering_by_created
 [X] 0003_alter_user_options
 [X] 0004_alter_user_managers
 [X] 0005_ensure_object_permission_names_are_unique
 [X] 0006_make_object_permission_name_globally_unique
 [X] 0007_alter_objectpermission_object_types
 [X] 0008_make_object_permission_a_changelogged_model
 [X] 0009_update_all_charfields_max_length_to_255
 [X] 0010_user_default_saved_views
virtualization
 [X] 0001_initial
 [X] 0002_virtualmachine_local_context_schema
 [X] 0003_vminterface_verbose_name
 [X] 0004_auto_slug
 [X] 0005_add_natural_indexing
 [X] 0006_vminterface_status
 [X] 0007_vminterface_status_data_migration
 [X] 0008_vminterface_parent
 [X] 0009_cluster_location
 [X] 0010_vminterface_mac_address_data_migration
 [X] 0011_alter_vminterface_mac_address
 [X] 0012_alter_virtualmachine_role_add_new_role
 [X] 0013_migrate_virtualmachine_role_data
 [X] 0014_rename_virtualmachine_roles
 [X] 0015_rename_foreignkey_fields
 [X] 0016_remove_site_foreign_key_from_cluster_class
 [X] 0017_created_datetime
 [X] 0018_related_name_changes
 [X] 0019_vminterface_ip_addresses_m2m
 [X] 0020_remove_clustergroup_clustertype_slug
 [X] 0021_tagsfield_and_vminterface_to_primarymodel
 [X] 0022_vminterface_timestamps_data_migration
 [X] 0023_ipam__namespaces
 [X] 0024_fixup_null_statuses
 [X] 0025_status_nonnullable
 [X] 0026_change_virtualmachine_primary_ip_fields
 [X] 0027_virtualmachine_software_image
 [X] 0028_update_all_charfields_max_length_to_255
 [X] 0029_add_role_field_to_interface_models
 [X] 0030_alter_virtualmachine_local_config_context_data_owner_content_type_and_more
wireless
 [X] 0001_initial
root@c8032ee34216:/source# 
```

We can see the last two `dcim` migrations were the two database models we created for `asset` and `maintenanceschedule`: 

```shell
 [X] 0067_controllermanageddevicegroup_tenant
 [X] 0068_asset
 [X] 0069_maintenanceschedule
```

Let us roll back the changes: 

```shell
root@c8032ee34216:/source# nautobot-server migrate dcim 0067_controllermanageddevicegroup_tenant
Operations to perform:
  Target specific migration: 0067_controllermanageddevicegroup_tenant, from dcim
Running migrations:
  Rendering model states... DONE
  Unapplying dcim.0069_maintenanceschedule... OK
  Unapplying dcim.0068_asset... OK
...
```

We can verify if the changes were indeed rolled back: 

```shell
root@c8032ee34216:/source# nautobot-server showmigrations dcim
dcim
 [X] 0001_initial_part_1
 [X] 0002_initial_part_2
 [X] 0003_initial_part_3
 [X] 0004_initial_part_4
 [X] 0005_device_local_context_schema
 [X] 0006_auto_slug
 [X] 0007_device_secrets_group
 [X] 0008_increase_all_serial_lengths
 [X] 0009_add_natural_indexing
 [X] 0010_interface_status
 [X] 0011_interface_status_data_migration
 [X] 0012_interface_parent_bridge
 [X] 0013_location_location_type
 [X] 0014_location_status_data_migration
 [X] 0015_device_components__changeloggedmodel
 [X] 0016_device_components__timestamp_data_migration
 [X] 0017_locationtype_nestable
 [X] 0018_device_redundancy_group
 [X] 0019_device_redundancy_group_data_migration
 [X] 0020_increase_device_asset_tag_size_limit
 [X] 0021_platform_network_driver
 [X] 0022_interface_redundancy_group
 [X] 0023_interface_redundancy_group_data_migration
 [X] 0024_move_site_fields_to_location_model
 [X] 0025_mptt_to_tree_queries
 [X] 0026_interface_mac_address_data_migration
 [X] 0027_alter_interface_mac_address
 [X] 0028_alter_device_and_rack_role_add_new_role
 [X] 0029_device_and_rack_roles_data_migrations
 [X] 0030_rename_device_and_rack_role
 [X] 0031_remove_device_role_and_rack_role
 [X] 0032_rename_foreignkey_fields
 [X] 0033_add_tree_managers_and_foreign_keys_pre_data_migration
 [X] 0034_migrate_region_and_site_data_to_locations
 [X] 0035_rename_path_end_point_related_name
 [X] 0036_remove_site_foreign_key_from_dcim_models
 [X] 0037_created_datetime
 [X] 0038_fixup_fks_and_related_names
 [X] 0039_related_name_changes
 [X] 0040_remove_region_and_site
 [X] 0041_interface_ip_addresses_m2m
 [X] 0042_alter_location_managers
 [X] 0043_remove_slug
 [X] 0044_tagsfield
 [X] 0045_ipam__namespaces
 [X] 0046_fixup_null_statuses
 [X] 0047_status_nonnullable
 [X] 0048_ensure_virtual_chassis_names_are_unique_and_add_uniqueness_constraint
 [X] 0049_remove_slugs_and_change_device_primary_ip_fields
 [X] 0050_fix_interface_redundancy_group_association_created
 [X] 0051_interface_redundancy_group_nullable_status
 [X] 0052_fix_interface_redundancy_group_created
 [X] 0053_create_device_family_model
 [X] 0054_softwareimage_softwareversion
 [X] 0055_softwareimage_softwareversion_data_migration
 [X] 0056_update_all_charfields_max_length_to_255
 [X] 0057_controller_models
 [X] 0058_controller_data_migration
 [X] 0059_add_role_field_to_interface_models
 [X] 0060_alter_cable_status_alter_consoleport__path_and_more
 [X] 0061_module_models
 [X] 0062_module_data_migration
 [X] 0063_interfacevdcassignment_virtualdevicecontext_and_more
 [X] 0064_virtualdevicecontext_status_data_migration
 [X] 0065_controller_capabilities_and_more
 [X] 0066_controllermanageddevicegroup_radio_profiles_and_more
 [X] 0067_controllermanageddevicegroup_tenant
 [ ] 0068_asset
 [ ] 0069_maintenanceschedule
```

Assuming we had to perform a rollback due to possible errors, we can now make the necessary changes and perform a `makemigrations` and `migrate` again. 

The ability to track database changes and rollback without knowing all the database commands was, and still is, one of Django's superpowers. 

Congratulations on completing Day 64! 

## Day 64 To Do

Remember to stop the codespace instance on [https://github.com/codespaces/](https://github.com/codespaces/). 

Go ahead and post a screenshot of a rollback for today's challenge on social media of your choice, make sure you use the tag `#100DaysOfNautobot` `#JobsToBeDone` and tag `@networktocode`, so we can share your progress! 

In tomorrow's challenge, we will be discussing database performance and scalability. See you tomorrow! 

[X/Twitter](<https://twitter.com/intent/tweet?url=https://github.com/nautobot/100-days-of-nautobot&text=I+just+completed+Day+64+of+the+100+days+of+nautobot+challenge+!&hashtags=100DaysOfNautobot,JobsToBeDone>)

[LinkedIn](https://www.linkedin.com/) (Copy & Paste: I just completed Day 64 of 100 Days of Nautobot, https://github.com/nautobot/100-days-of-nautobot, challenge! @networktocode #JobsToBeDone #100DaysOfNautobot) 
