# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WAL.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import HBase_pb2 as HBase__pb2
from . import Client_pb2 as Client__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WAL.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\tWAL.proto\x1a\x0bHBase.proto\x1a\x0c\x43lient.proto\"\x8f\x01\n\tWALHeader\x12\x17\n\x0fhas_compression\x18\x01 \x01(\x08\x12\x16\n\x0e\x65ncryption_key\x18\x02 \x01(\x0c\x12\x1b\n\x13has_tag_compression\x18\x03 \x01(\x08\x12\x17\n\x0fwriter_cls_name\x18\x04 \x01(\t\x12\x1b\n\x13\x63\x65ll_codec_cls_name\x18\x05 \x01(\t\"\xa0\x02\n\x06WALKey\x12\x1b\n\x13\x65ncoded_region_name\x18\x01 \x02(\x0c\x12\x12\n\ntable_name\x18\x02 \x02(\x0c\x12\x1b\n\x13log_sequence_number\x18\x03 \x02(\x04\x12\x12\n\nwrite_time\x18\x04 \x02(\x04\x12\x1d\n\ncluster_id\x18\x05 \x01(\x0b\x32\x05.UUIDB\x02\x18\x01\x12\x1c\n\x06scopes\x18\x06 \x03(\x0b\x32\x0c.FamilyScope\x12\x1a\n\x12\x66ollowing_kv_count\x18\x07 \x01(\r\x12\x1a\n\x0b\x63luster_ids\x18\x08 \x03(\x0b\x32\x05.UUID\x12\x12\n\nnonceGroup\x18\t \x01(\x04\x12\r\n\x05nonce\x18\n \x01(\x04\x12\x1c\n\x14orig_sequence_number\x18\x0b \x01(\x04\"=\n\x0b\x46\x61milyScope\x12\x0e\n\x06\x66\x61mily\x18\x01 \x02(\x0c\x12\x1e\n\nscope_type\x18\x02 \x02(\x0e\x32\n.ScopeType\"\xbe\x01\n\x14\x43ompactionDescriptor\x12\x12\n\ntable_name\x18\x01 \x02(\x0c\x12\x1b\n\x13\x65ncoded_region_name\x18\x02 \x02(\x0c\x12\x13\n\x0b\x66\x61mily_name\x18\x03 \x02(\x0c\x12\x18\n\x10\x63ompaction_input\x18\x04 \x03(\t\x12\x19\n\x11\x63ompaction_output\x18\x05 \x03(\t\x12\x16\n\x0estore_home_dir\x18\x06 \x02(\t\x12\x13\n\x0bregion_name\x18\x07 \x01(\x0c\"\x92\x03\n\x0f\x46lushDescriptor\x12,\n\x06\x61\x63tion\x18\x01 \x02(\x0e\x32\x1c.FlushDescriptor.FlushAction\x12\x12\n\ntable_name\x18\x02 \x02(\x0c\x12\x1b\n\x13\x65ncoded_region_name\x18\x03 \x02(\x0c\x12\x1d\n\x15\x66lush_sequence_number\x18\x04 \x01(\x04\x12<\n\rstore_flushes\x18\x05 \x03(\x0b\x32%.FlushDescriptor.StoreFlushDescriptor\x12\x13\n\x0bregion_name\x18\x06 \x01(\x0c\x1aY\n\x14StoreFlushDescriptor\x12\x13\n\x0b\x66\x61mily_name\x18\x01 \x02(\x0c\x12\x16\n\x0estore_home_dir\x18\x02 \x02(\t\x12\x14\n\x0c\x66lush_output\x18\x03 \x03(\t\"S\n\x0b\x46lushAction\x12\x0f\n\x0bSTART_FLUSH\x10\x00\x12\x10\n\x0c\x43OMMIT_FLUSH\x10\x01\x12\x0f\n\x0b\x41\x42ORT_FLUSH\x10\x02\x12\x10\n\x0c\x43\x41NNOT_FLUSH\x10\x03\"R\n\x0fStoreDescriptor\x12\x13\n\x0b\x66\x61mily_name\x18\x01 \x02(\x0c\x12\x16\n\x0estore_home_dir\x18\x02 \x02(\t\x12\x12\n\nstore_file\x18\x03 \x03(\t\"\x8d\x01\n\x12\x42ulkLoadDescriptor\x12\x1e\n\ntable_name\x18\x01 \x02(\x0b\x32\n.TableName\x12\x1b\n\x13\x65ncoded_region_name\x18\x02 \x02(\x0c\x12 \n\x06stores\x18\x03 \x03(\x0b\x32\x10.StoreDescriptor\x12\x18\n\x10\x62ulkload_seq_num\x18\x04 \x02(\x03\"\x9f\x02\n\x15RegionEventDescriptor\x12\x34\n\nevent_type\x18\x01 \x02(\x0e\x32 .RegionEventDescriptor.EventType\x12\x12\n\ntable_name\x18\x02 \x02(\x0c\x12\x1b\n\x13\x65ncoded_region_name\x18\x03 \x02(\x0c\x12\x1b\n\x13log_sequence_number\x18\x04 \x01(\x04\x12 \n\x06stores\x18\x05 \x03(\x0b\x32\x10.StoreDescriptor\x12\x1b\n\x06server\x18\x06 \x01(\x0b\x32\x0b.ServerName\x12\x13\n\x0bregion_name\x18\x07 \x01(\x0c\".\n\tEventType\x12\x0f\n\x0bREGION_OPEN\x10\x00\x12\x10\n\x0cREGION_CLOSE\x10\x01\"\x0c\n\nWALTrailer*F\n\tScopeType\x12\x1b\n\x17REPLICATION_SCOPE_LOCAL\x10\x00\x12\x1c\n\x18REPLICATION_SCOPE_GLOBAL\x10\x01\x42?\n*org.apache.hadoop.hbase.protobuf.generatedB\tWALProtosH\x01\x88\x01\x00\xa0\x01\x01')
  ,
  dependencies=[HBase__pb2.DESCRIPTOR,Client__pb2.DESCRIPTOR,])

_SCOPETYPE = _descriptor.EnumDescriptor(
  name='ScopeType',
  full_name='ScopeType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='REPLICATION_SCOPE_LOCAL', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REPLICATION_SCOPE_GLOBAL', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1670,
  serialized_end=1740,
)
_sym_db.RegisterEnumDescriptor(_SCOPETYPE)

ScopeType = enum_type_wrapper.EnumTypeWrapper(_SCOPETYPE)
REPLICATION_SCOPE_LOCAL = 0
REPLICATION_SCOPE_GLOBAL = 1


_FLUSHDESCRIPTOR_FLUSHACTION = _descriptor.EnumDescriptor(
  name='FlushAction',
  full_name='FlushDescriptor.FlushAction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='START_FLUSH', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMMIT_FLUSH', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ABORT_FLUSH', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANNOT_FLUSH', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1053,
  serialized_end=1136,
)
_sym_db.RegisterEnumDescriptor(_FLUSHDESCRIPTOR_FLUSHACTION)

_REGIONEVENTDESCRIPTOR_EVENTTYPE = _descriptor.EnumDescriptor(
  name='EventType',
  full_name='RegionEventDescriptor.EventType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='REGION_OPEN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REGION_CLOSE', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1608,
  serialized_end=1654,
)
_sym_db.RegisterEnumDescriptor(_REGIONEVENTDESCRIPTOR_EVENTTYPE)


_WALHEADER = _descriptor.Descriptor(
  name='WALHeader',
  full_name='WALHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='has_compression', full_name='WALHeader.has_compression', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='encryption_key', full_name='WALHeader.encryption_key', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='has_tag_compression', full_name='WALHeader.has_tag_compression', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='writer_cls_name', full_name='WALHeader.writer_cls_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cell_codec_cls_name', full_name='WALHeader.cell_codec_cls_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=41,
  serialized_end=184,
)


_WALKEY = _descriptor.Descriptor(
  name='WALKey',
  full_name='WALKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='encoded_region_name', full_name='WALKey.encoded_region_name', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='table_name', full_name='WALKey.table_name', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='log_sequence_number', full_name='WALKey.log_sequence_number', index=2,
      number=3, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='write_time', full_name='WALKey.write_time', index=3,
      number=4, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cluster_id', full_name='WALKey.cluster_id', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scopes', full_name='WALKey.scopes', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='following_kv_count', full_name='WALKey.following_kv_count', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cluster_ids', full_name='WALKey.cluster_ids', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nonceGroup', full_name='WALKey.nonceGroup', index=8,
      number=9, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nonce', full_name='WALKey.nonce', index=9,
      number=10, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orig_sequence_number', full_name='WALKey.orig_sequence_number', index=10,
      number=11, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=187,
  serialized_end=475,
)


_FAMILYSCOPE = _descriptor.Descriptor(
  name='FamilyScope',
  full_name='FamilyScope',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='family', full_name='FamilyScope.family', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scope_type', full_name='FamilyScope.scope_type', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=477,
  serialized_end=538,
)


_COMPACTIONDESCRIPTOR = _descriptor.Descriptor(
  name='CompactionDescriptor',
  full_name='CompactionDescriptor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='table_name', full_name='CompactionDescriptor.table_name', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='encoded_region_name', full_name='CompactionDescriptor.encoded_region_name', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='family_name', full_name='CompactionDescriptor.family_name', index=2,
      number=3, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='compaction_input', full_name='CompactionDescriptor.compaction_input', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='compaction_output', full_name='CompactionDescriptor.compaction_output', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='store_home_dir', full_name='CompactionDescriptor.store_home_dir', index=5,
      number=6, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='region_name', full_name='CompactionDescriptor.region_name', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=541,
  serialized_end=731,
)


_FLUSHDESCRIPTOR_STOREFLUSHDESCRIPTOR = _descriptor.Descriptor(
  name='StoreFlushDescriptor',
  full_name='FlushDescriptor.StoreFlushDescriptor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='family_name', full_name='FlushDescriptor.StoreFlushDescriptor.family_name', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='store_home_dir', full_name='FlushDescriptor.StoreFlushDescriptor.store_home_dir', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flush_output', full_name='FlushDescriptor.StoreFlushDescriptor.flush_output', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=962,
  serialized_end=1051,
)

_FLUSHDESCRIPTOR = _descriptor.Descriptor(
  name='FlushDescriptor',
  full_name='FlushDescriptor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='FlushDescriptor.action', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='table_name', full_name='FlushDescriptor.table_name', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='encoded_region_name', full_name='FlushDescriptor.encoded_region_name', index=2,
      number=3, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flush_sequence_number', full_name='FlushDescriptor.flush_sequence_number', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='store_flushes', full_name='FlushDescriptor.store_flushes', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='region_name', full_name='FlushDescriptor.region_name', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_FLUSHDESCRIPTOR_STOREFLUSHDESCRIPTOR, ],
  enum_types=[
    _FLUSHDESCRIPTOR_FLUSHACTION,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=734,
  serialized_end=1136,
)


_STOREDESCRIPTOR = _descriptor.Descriptor(
  name='StoreDescriptor',
  full_name='StoreDescriptor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='family_name', full_name='StoreDescriptor.family_name', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='store_home_dir', full_name='StoreDescriptor.store_home_dir', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='store_file', full_name='StoreDescriptor.store_file', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1138,
  serialized_end=1220,
)


_BULKLOADDESCRIPTOR = _descriptor.Descriptor(
  name='BulkLoadDescriptor',
  full_name='BulkLoadDescriptor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='table_name', full_name='BulkLoadDescriptor.table_name', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='encoded_region_name', full_name='BulkLoadDescriptor.encoded_region_name', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stores', full_name='BulkLoadDescriptor.stores', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bulkload_seq_num', full_name='BulkLoadDescriptor.bulkload_seq_num', index=3,
      number=4, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1223,
  serialized_end=1364,
)


_REGIONEVENTDESCRIPTOR = _descriptor.Descriptor(
  name='RegionEventDescriptor',
  full_name='RegionEventDescriptor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event_type', full_name='RegionEventDescriptor.event_type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='table_name', full_name='RegionEventDescriptor.table_name', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='encoded_region_name', full_name='RegionEventDescriptor.encoded_region_name', index=2,
      number=3, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='log_sequence_number', full_name='RegionEventDescriptor.log_sequence_number', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stores', full_name='RegionEventDescriptor.stores', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='server', full_name='RegionEventDescriptor.server', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='region_name', full_name='RegionEventDescriptor.region_name', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REGIONEVENTDESCRIPTOR_EVENTTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1367,
  serialized_end=1654,
)


_WALTRAILER = _descriptor.Descriptor(
  name='WALTrailer',
  full_name='WALTrailer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1656,
  serialized_end=1668,
)

_WALKEY.fields_by_name['cluster_id'].message_type = HBase__pb2._UUID
_WALKEY.fields_by_name['scopes'].message_type = _FAMILYSCOPE
_WALKEY.fields_by_name['cluster_ids'].message_type = HBase__pb2._UUID
_FAMILYSCOPE.fields_by_name['scope_type'].enum_type = _SCOPETYPE
_FLUSHDESCRIPTOR_STOREFLUSHDESCRIPTOR.containing_type = _FLUSHDESCRIPTOR
_FLUSHDESCRIPTOR.fields_by_name['action'].enum_type = _FLUSHDESCRIPTOR_FLUSHACTION
_FLUSHDESCRIPTOR.fields_by_name['store_flushes'].message_type = _FLUSHDESCRIPTOR_STOREFLUSHDESCRIPTOR
_FLUSHDESCRIPTOR_FLUSHACTION.containing_type = _FLUSHDESCRIPTOR
_BULKLOADDESCRIPTOR.fields_by_name['table_name'].message_type = HBase__pb2._TABLENAME
_BULKLOADDESCRIPTOR.fields_by_name['stores'].message_type = _STOREDESCRIPTOR
_REGIONEVENTDESCRIPTOR.fields_by_name['event_type'].enum_type = _REGIONEVENTDESCRIPTOR_EVENTTYPE
_REGIONEVENTDESCRIPTOR.fields_by_name['stores'].message_type = _STOREDESCRIPTOR
_REGIONEVENTDESCRIPTOR.fields_by_name['server'].message_type = HBase__pb2._SERVERNAME
_REGIONEVENTDESCRIPTOR_EVENTTYPE.containing_type = _REGIONEVENTDESCRIPTOR
DESCRIPTOR.message_types_by_name['WALHeader'] = _WALHEADER
DESCRIPTOR.message_types_by_name['WALKey'] = _WALKEY
DESCRIPTOR.message_types_by_name['FamilyScope'] = _FAMILYSCOPE
DESCRIPTOR.message_types_by_name['CompactionDescriptor'] = _COMPACTIONDESCRIPTOR
DESCRIPTOR.message_types_by_name['FlushDescriptor'] = _FLUSHDESCRIPTOR
DESCRIPTOR.message_types_by_name['StoreDescriptor'] = _STOREDESCRIPTOR
DESCRIPTOR.message_types_by_name['BulkLoadDescriptor'] = _BULKLOADDESCRIPTOR
DESCRIPTOR.message_types_by_name['RegionEventDescriptor'] = _REGIONEVENTDESCRIPTOR
DESCRIPTOR.message_types_by_name['WALTrailer'] = _WALTRAILER
DESCRIPTOR.enum_types_by_name['ScopeType'] = _SCOPETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WALHeader = _reflection.GeneratedProtocolMessageType('WALHeader', (_message.Message,), dict(
  DESCRIPTOR = _WALHEADER,
  __module__ = 'WAL_pb2'
  # @@protoc_insertion_point(class_scope:WALHeader)
  ))
_sym_db.RegisterMessage(WALHeader)

WALKey = _reflection.GeneratedProtocolMessageType('WALKey', (_message.Message,), dict(
  DESCRIPTOR = _WALKEY,
  __module__ = 'WAL_pb2'
  # @@protoc_insertion_point(class_scope:WALKey)
  ))
_sym_db.RegisterMessage(WALKey)

FamilyScope = _reflection.GeneratedProtocolMessageType('FamilyScope', (_message.Message,), dict(
  DESCRIPTOR = _FAMILYSCOPE,
  __module__ = 'WAL_pb2'
  # @@protoc_insertion_point(class_scope:FamilyScope)
  ))
_sym_db.RegisterMessage(FamilyScope)

CompactionDescriptor = _reflection.GeneratedProtocolMessageType('CompactionDescriptor', (_message.Message,), dict(
  DESCRIPTOR = _COMPACTIONDESCRIPTOR,
  __module__ = 'WAL_pb2'
  # @@protoc_insertion_point(class_scope:CompactionDescriptor)
  ))
_sym_db.RegisterMessage(CompactionDescriptor)

FlushDescriptor = _reflection.GeneratedProtocolMessageType('FlushDescriptor', (_message.Message,), dict(

  StoreFlushDescriptor = _reflection.GeneratedProtocolMessageType('StoreFlushDescriptor', (_message.Message,), dict(
    DESCRIPTOR = _FLUSHDESCRIPTOR_STOREFLUSHDESCRIPTOR,
    __module__ = 'WAL_pb2'
    # @@protoc_insertion_point(class_scope:FlushDescriptor.StoreFlushDescriptor)
    ))
  ,
  DESCRIPTOR = _FLUSHDESCRIPTOR,
  __module__ = 'WAL_pb2'
  # @@protoc_insertion_point(class_scope:FlushDescriptor)
  ))
_sym_db.RegisterMessage(FlushDescriptor)
_sym_db.RegisterMessage(FlushDescriptor.StoreFlushDescriptor)

StoreDescriptor = _reflection.GeneratedProtocolMessageType('StoreDescriptor', (_message.Message,), dict(
  DESCRIPTOR = _STOREDESCRIPTOR,
  __module__ = 'WAL_pb2'
  # @@protoc_insertion_point(class_scope:StoreDescriptor)
  ))
_sym_db.RegisterMessage(StoreDescriptor)

BulkLoadDescriptor = _reflection.GeneratedProtocolMessageType('BulkLoadDescriptor', (_message.Message,), dict(
  DESCRIPTOR = _BULKLOADDESCRIPTOR,
  __module__ = 'WAL_pb2'
  # @@protoc_insertion_point(class_scope:BulkLoadDescriptor)
  ))
_sym_db.RegisterMessage(BulkLoadDescriptor)

RegionEventDescriptor = _reflection.GeneratedProtocolMessageType('RegionEventDescriptor', (_message.Message,), dict(
  DESCRIPTOR = _REGIONEVENTDESCRIPTOR,
  __module__ = 'WAL_pb2'
  # @@protoc_insertion_point(class_scope:RegionEventDescriptor)
  ))
_sym_db.RegisterMessage(RegionEventDescriptor)

WALTrailer = _reflection.GeneratedProtocolMessageType('WALTrailer', (_message.Message,), dict(
  DESCRIPTOR = _WALTRAILER,
  __module__ = 'WAL_pb2'
  # @@protoc_insertion_point(class_scope:WALTrailer)
  ))
_sym_db.RegisterMessage(WALTrailer)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n*org.apache.hadoop.hbase.protobuf.generatedB\tWALProtosH\001\210\001\000\240\001\001'))
_WALKEY.fields_by_name['cluster_id'].has_options = True
_WALKEY.fields_by_name['cluster_id']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))
# @@protoc_insertion_point(module_scope)
