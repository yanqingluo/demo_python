# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dzhyun.dxspirit.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='dzhyun.dxspirit.proto',
  package='dzhyun',
  syntax='proto2',
  serialized_pb=_b('\n\x15\x64zhyun.dxspirit.proto\x12\x06\x64zhyun\"H\n\x08\x44XSpirit\x12\x0f\n\x07ShiJian\x18\x01 \x02(\x03\x12\x0b\n\x03Obj\x18\x02 \x01(\t\x12\x0f\n\x07TongZhi\x18\x03 \x01(\t\x12\r\n\x05ShuJu\x18\x04 \x01(\x03\"\xa1\x04\n\x0c\x44XSpiritStat\x12\x0b\n\x03Obj\x18\x01 \x01(\t\x12\x11\n\tHjfsTotal\x18\x02 \x01(\x03\x12\x11\n\tKsftTotal\x18\x03 \x01(\x03\x12\x11\n\tGttsTotal\x18\x04 \x01(\x03\x12\x11\n\tJsxdTotal\x18\x05 \x01(\x03\x12\x11\n\tDbmrTotal\x18\x06 \x01(\x03\x12\x16\n\x0e\x44\x62mrStatistics\x18\x07 \x01(\x03\x12\x11\n\tDbmcTotal\x18\x08 \x01(\x03\x12\x16\n\x0e\x44\x62mcStatistics\x18\t \x01(\x03\x12\x11\n\tFztbTotal\x18\n \x01(\x03\x12\x11\n\tFdtbTotal\x18\x0b \x01(\x03\x12\x11\n\tDkztTotal\x18\x0c \x01(\x03\x12\x11\n\tDkdtTotal\x18\r \x01(\x03\x12\x12\n\nYdmcPTotal\x18\x0e \x01(\x03\x12\x12\n\nYdmrPTotal\x18\x0f \x01(\x03\x12\x11\n\tLszsTotal\x18\x10 \x01(\x03\x12\x11\n\tDyzsTotal\x18\x11 \x01(\x03\x12\x13\n\x0bJgmrgdTotal\x18\x12 \x01(\x03\x12\x13\n\x0bJgmcgdTotal\x18\x13 \x01(\x03\x12\x13\n\x0b\x44\x63jmrdTotal\x18\x14 \x01(\x03\x12\x13\n\x0b\x44\x63jmcdTotal\x18\x15 \x01(\x03\x12\x13\n\x0b\x46\x64mrgdTotal\x18\x16 \x01(\x03\x12\x13\n\x0b\x46\x64mcgdTotal\x18\x17 \x01(\x03\x12\x11\n\tMrcdTotal\x18\x18 \x01(\x03\x12\x11\n\tMccdTotal\x18\x19 \x01(\x03\x12\x11\n\tMrxdTotal\x18\x1a \x01(\x03\x12\x11\n\tMcxdTotal\x18\x1b \x01(\x03\x42\x12\n\x10\x63om.dzhyun.proto')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DXSPIRIT = _descriptor.Descriptor(
  name='DXSpirit',
  full_name='dzhyun.DXSpirit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ShiJian', full_name='dzhyun.DXSpirit.ShiJian', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Obj', full_name='dzhyun.DXSpirit.Obj', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TongZhi', full_name='dzhyun.DXSpirit.TongZhi', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ShuJu', full_name='dzhyun.DXSpirit.ShuJu', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=33,
  serialized_end=105,
)


_DXSPIRITSTAT = _descriptor.Descriptor(
  name='DXSpiritStat',
  full_name='dzhyun.DXSpiritStat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Obj', full_name='dzhyun.DXSpiritStat.Obj', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='HjfsTotal', full_name='dzhyun.DXSpiritStat.HjfsTotal', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='KsftTotal', full_name='dzhyun.DXSpiritStat.KsftTotal', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='GttsTotal', full_name='dzhyun.DXSpiritStat.GttsTotal', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='JsxdTotal', full_name='dzhyun.DXSpiritStat.JsxdTotal', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='DbmrTotal', full_name='dzhyun.DXSpiritStat.DbmrTotal', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='DbmrStatistics', full_name='dzhyun.DXSpiritStat.DbmrStatistics', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='DbmcTotal', full_name='dzhyun.DXSpiritStat.DbmcTotal', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='DbmcStatistics', full_name='dzhyun.DXSpiritStat.DbmcStatistics', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='FztbTotal', full_name='dzhyun.DXSpiritStat.FztbTotal', index=9,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='FdtbTotal', full_name='dzhyun.DXSpiritStat.FdtbTotal', index=10,
      number=11, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='DkztTotal', full_name='dzhyun.DXSpiritStat.DkztTotal', index=11,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='DkdtTotal', full_name='dzhyun.DXSpiritStat.DkdtTotal', index=12,
      number=13, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='YdmcPTotal', full_name='dzhyun.DXSpiritStat.YdmcPTotal', index=13,
      number=14, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='YdmrPTotal', full_name='dzhyun.DXSpiritStat.YdmrPTotal', index=14,
      number=15, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='LszsTotal', full_name='dzhyun.DXSpiritStat.LszsTotal', index=15,
      number=16, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='DyzsTotal', full_name='dzhyun.DXSpiritStat.DyzsTotal', index=16,
      number=17, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='JgmrgdTotal', full_name='dzhyun.DXSpiritStat.JgmrgdTotal', index=17,
      number=18, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='JgmcgdTotal', full_name='dzhyun.DXSpiritStat.JgmcgdTotal', index=18,
      number=19, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='DcjmrdTotal', full_name='dzhyun.DXSpiritStat.DcjmrdTotal', index=19,
      number=20, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='DcjmcdTotal', full_name='dzhyun.DXSpiritStat.DcjmcdTotal', index=20,
      number=21, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='FdmrgdTotal', full_name='dzhyun.DXSpiritStat.FdmrgdTotal', index=21,
      number=22, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='FdmcgdTotal', full_name='dzhyun.DXSpiritStat.FdmcgdTotal', index=22,
      number=23, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MrcdTotal', full_name='dzhyun.DXSpiritStat.MrcdTotal', index=23,
      number=24, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MccdTotal', full_name='dzhyun.DXSpiritStat.MccdTotal', index=24,
      number=25, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MrxdTotal', full_name='dzhyun.DXSpiritStat.MrxdTotal', index=25,
      number=26, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='McxdTotal', full_name='dzhyun.DXSpiritStat.McxdTotal', index=26,
      number=27, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=108,
  serialized_end=653,
)

DESCRIPTOR.message_types_by_name['DXSpirit'] = _DXSPIRIT
DESCRIPTOR.message_types_by_name['DXSpiritStat'] = _DXSPIRITSTAT

DXSpirit = _reflection.GeneratedProtocolMessageType('DXSpirit', (_message.Message,), dict(
  DESCRIPTOR = _DXSPIRIT,
  __module__ = 'dzhyun.dxspirit_pb2'
  # @@protoc_insertion_point(class_scope:dzhyun.DXSpirit)
  ))
_sym_db.RegisterMessage(DXSpirit)

DXSpiritStat = _reflection.GeneratedProtocolMessageType('DXSpiritStat', (_message.Message,), dict(
  DESCRIPTOR = _DXSPIRITSTAT,
  __module__ = 'dzhyun.dxspirit_pb2'
  # @@protoc_insertion_point(class_scope:dzhyun.DXSpiritStat)
  ))
_sym_db.RegisterMessage(DXSpiritStat)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\020com.dzhyun.proto'))
# @@protoc_insertion_point(module_scope)