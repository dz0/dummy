#@inline 1: test_mytracer. None 
def test():
    dfa1, dfq1, dfm1 = get_dataframes(csvfile1, spec1)
    #@inline 2: test_mytracer. None 
    def get_dataframes(csvfile, spec=SPEC):
        tables = [t for csv_segment, pdef in Reader(csvfile, spec).items()
        #@inline 3: csv2df.reader. Reader.__init__ 
        def __init__(self, csvfile, spec):
            self.rows = list(to_rows(csvfile))
            #@inline 4: csv2df.reader. None 
            def to_rows(csvfile):
                csv_rows = yield_csv_rows(csvfile)
                csv_rows = filter_csv_rows(csv_rows)
                #@inline 5: csv2df.reader. None 
                def filter_csv_rows(gen):
                    filled = filter(lambda row: row and row[0], gen)
                    no_comments = filter(lambda row: not row[0].startswith("___"), filled)
                    return no_comments
                #@return: filter_csv_rows => <filter object at 0x7f7be9d3d0...
                return map(Row, csv_rows)
            #@return: to_rows => <map object at 0x7f7bdbc2b2b0>
                #@inline 4: csv2df.reader. None 
                def yield_csv_rows(csvfile, fmt=CSV_FORMAT):
                    for row in csv.reader(csvfile, **fmt):
                        yield row
                #@return: yield_csv_rows => []
                        #@inline 4: csv2df.reader. None 
                        filled = filter(lambda row: row and row[0], gen)
                        #@inline 5: csv2df.reader. None 
                        no_comments = filter(lambda row: not row[0].startswith("___"), filled)
                        #@inline 6: csv2df.reader. Row.__init__ 
                        def __init__(self, row):
                            self.name = row[0]
                            self.data = row[1:]
                        #@return: __init__ => None
                        #@return: yield_csv_rows => None
                            self.spec = spec
                        #@return: __init__ => None
                            #@inline 4: csv2df.reader. Reader.items 
                            def items(self):
                                rowstack = RowStack(self.rows)
                                #@inline 5: csv2df.reader. RowStack.__init__ 
                                def __init__(self, rows):
                                    self.rows = list(rows)
                                #@return: __init__ => None
                                return rowstack.yield_segment_with_defintion(self.spec)
                            #@return: items => <generator object RowStack.yie...
                                #@inline 4: test_mytracer. None 
                                def get_dataframes(csvfile, spec=SPEC):
                                #@inline 5: csv2df.reader. RowStack.yield_segment_with_defintion 
                                def yield_segment_with_defintion(self, spec):
                                    for pdef in spec.get_segment_parsing_definitions():
                                    #@inline 6: csv2df.specification. Specification.get_segment_parsing_definitions 
                                    def get_segment_parsing_definitions(self):
                                        return self.segment_definitions
                                    #@return: get_segment_parsing_definitions => []
                                    yield self.remaining_rows(), spec.get_main_parsing_definition()
                                    #@inline 6: csv2df.reader. RowStack.remaining_rows 
                                    def remaining_rows(self):
                                        remaining = self.rows
                                        self.rows = []
                                        return remaining
                                    #@return: remaining_rows => [Row(['1. Сводные показатели /...
                                        #@inline 6: csv2df.specification. Specification.get_main_parsing_definition 
                                        def get_main_parsing_definition(self):
                                            return self.main
                                        #@return: get_main_parsing_definition => <csv2df.specification.Definiti...
                                #@return: yield_segment_with_defintion => ([Row(['1. Сводные показатели ...
                                              for t in extract_tables(csv_segment, pdef)]
                                              #@inline 5: csv2df.parser. None 
                                              def extract_tables(csv_segment, pdef):
                                                  tables = split_to_tables(csv_segment)
                                                  tables = parse_tables(tables, pdef)
                                                  #@inline 6: csv2df.parser. None 
                                                  def parse_tables(tables, pdef):
                                                      tables = [t.set_label(pdef.varnames_dict, pdef.units_dict) for t in tables]
                                                      #@inline 7: csv2df.parser. None 
                                                      def parse_tables(tables, pdef):
                                                      #@inline 8: csv2df.parser. None 
                                                      def split_to_tables(rows):
                                                          datarows = []
                                                          headers = []
                                                          state = State.INIT
                                                          for row in rows:
                                                              if row.is_datarow():
                                                              #@inline 9: csv2df.reader. Row.is_datarow 
                                                              def is_datarow(self):
                                                                  return is_year(self.name)
                                                                  #@inline 10: csv2df.reader. None 
                                                                  def is_year(string: str) -> bool:
                                                                      return get_year(string) is not False
                                                                      #@inline 11: csv2df.reader. None 
                                                                      def get_year(string: str, rx=YEAR_CATCHER):
                                                                          match = re.match(rx, string)
                                                                          if match:
                                                                          return False
                                                                      #@return: get_year => False
                                                                  #@return: is_year => False
                                                              #@return: is_datarow => False
                                                                  if state == State.DATA:  # table ended
                                                                  headers.append(row)
                                                                  state = State.UNKNOWN
                                                              year = int(match.group(1))
                                                              if year >= 1991 and year <= 2050:
                                                                  return year
                                                      #@return: get_year => 2015
                                                                  datarows.append(row)
                                                                  state = State.DATA
                                                                      yield Table(headers, datarows)
                                                                      #@inline 8: csv2df.parser. Table.__init__ 
                                                                      def __init__(self, headers, datarows):
                                                                          self.varname = None
                                                                          self.unit = None
                                                                          self.headers = headers
                                                                          self.lines = odict((row.name, self.UNKNOWN) for row in headers)
                                                                          #@inline 9: csv2df.parser. None 
                                                                          def __init__(self, headers, datarows):
                                                                              self.datarows = datarows
                                                                              self.coln = max(len(row) for row in self.datarows)
                                                                              #@inline 10: csv2df.parser. None 
                                                                              def __init__(self, headers, datarows):
                                                                              #@inline 11: csv2df.reader. Row.__len__ 
                                                                              def __len__(self):
                                                                                  return len(self.data)
                                                                              #@return: __len__ => 5
                                                                                  self.splitter_func = None
                                                                              #@return: __init__ => None
                                                                          #@return: split_to_tables => Table None (5 columns)
- <1. С...
                                                                                  #@inline 9: csv2df.specification. None 
                                                                                  @property
                                                                                      return self.instr.varname_mapper
                                                                                  #@return: varnames_dict => OrderedDict([('Объем ВВП', 'GD...
                                                                                      #@inline 9: csv2df.specification. None 
                                                                                      @property
                                                                                          return self.units
                                                                                      #@return: units_dict => {'млрд.рублей': 'bln_rub', 'пе...
                                                                                          #@inline 9: csv2df.parser. Table.set_label 
                                                                                          def set_label(self, varnames_dict, units_dict):
                                                                                              for row in self.headers:
                                                                                                  varname = row.get_varname(varnames_dict)
                                                                                                  #@inline 10: csv2df.reader. Row.get_varname 
                                                                                                  def get_varname(self, varnames_mapper_dict):
                                                                                                      varnames = []
                                                                                                      for k in varnames_mapper_dict.keys():
                                                                                                          if self.matches(k):
                                                                                                          #@inline 11: csv2df.reader. Row.matches 
                                                                                                          def matches(self, pat):
                                                                                                              rx = r"\b{}".format(pat)
                                                                                                              return bool(re.search(rx, self.name))
                                                                                                          #@return: matches => False
                                                                                                      if len(varnames) > 1:
                                                                                                      elif len(varnames) == 1:
                                                                                                          return False
                                                                                                  #@return: get_varname => False
                                                                                                  if varname:
                                                                                                  unit = row.get_unit(units_dict)
                                                                                                  #@inline 10: csv2df.reader. Row.get_unit 
                                                                                                  def get_unit(self, units_mapper_dict):
                                                                                                      for k in units_mapper_dict.keys():
                                                                                                          if k in self.name:
                                                                                                      return False
                                                                                                  #@return: get_unit => False
                                                                                                  if unit:
                                                                                                      varnames.append(varnames_mapper_dict[k])
                                                                                                  return varnames[0]
                                                                                          #@return: get_varname => GDP
                                                                                  self.varname = varname
                                                                                  self.lines[row.name] = self.KNOWN
                                                                                  return units_mapper_dict[k]
                                                                      #@return: get_unit => bln_rub
                                                                      self.unit = unit
                                                                      self.lines[row.name] = self.KNOWN
                                                              return self
                                                      #@return: set_label => Table GDP_bln_rub (5 columns)
...
                                                                  headers = []
                                                                  datarows = []
                                                      if len(headers) > 0 and len(datarows) > 0:
                                                  #@return: split_to_tables => None
                                                  tables = [t.set_splitter(pdef.funcname) for t in tables]
                                                  #@inline 6: csv2df.parser. None 
                                                  def parse_tables(tables, pdef):
                                                  #@inline 7: csv2df.specification. None 
                                                  @property
                                                      return self.reader
                                                  #@return: funcname => False
                                                      #@inline 7: csv2df.parser. Table.set_splitter 
                                                      def set_splitter(self, funcname):
                                                          self.splitter_func = splitter.get_splitter(funcname or self.coln)
                                                          #@inline 8: csv2df.util_row_splitter. None 
                                                          def get_splitter(arg):
                                                              try:
                                                                  return FUNC_MAPPER[arg]
                                                          #@return: get_splitter => <function split_row_by_year_an...
                                                          return self
                                                      #@return: set_splitter => Table GDP_bln_rub (5 columns)
...
                                                      def fix_multitable_units(tables):
                                                      fix_multitable_units(tables)
                                                      #@inline 7: csv2df.parser. None 
                                                      def fix_multitable_units(tables):
                                                          for prev_table, table in zip(tables, tables[1:]):
                                                              if table.varname is None and not table.has_unknown_lines():
                                                              #@inline 8: csv2df.parser. Table.has_unknown_lines 
                                                              def has_unknown_lines(self):
                                                                  return self.UNKNOWN in self.lines.values()
                                                              #@return: has_unknown_lines => False
                                                                  table.varname = prev_table.varname
                                                      #@return: fix_multitable_units => None
                                                      return tables
                                                  #@return: parse_tables => [Table(headers=[Row(['1. Сводн...
                                                  verify_tables(tables, pdef)
                                                  #@inline 6: csv2df.parser. None 
                                                  def verify_tables(tables, pdef):
                                                      _labels_in_tables = [t.label for t in tables]
                                                      #@inline 7: csv2df.parser. None 
                                                      def verify_tables(tables, pdef):
                                                      #@inline 8: csv2df.parser. None 
                                                      @property
                                                          vn = self.varname
                                                          u = self.unit
                                                          if vn and u:
                                                              return make_label(vn, u)
                                                              #@inline 9: csv2df.util_label. None 
                                                              def make_label(vn, unit, sep=SEP):
                                                                  return vn + sep + unit
                                                              #@return: make_label => GDP_bln_rub
                                                      #@return: label => GDP_bln_rub
                                                          _labels_missed = [x for x in pdef.required if x not in _labels_in_tables]
                                                          #@inline 8: csv2df.specification. None 
                                                          @property
                                                              return self.instr.required_labels
                                                          #@return: required => ['GDP_bln_rub', 'INDPRO_yoy', ...
                                                              #@inline 8: csv2df.parser. None 
                                                              def verify_tables(tables, pdef):
                                                                  if _labels_missed:
                                                              #@return: verify_tables => None
                                                          return [t for t in tables if t.label in pdef.required]
                                                          #@inline 8: csv2df.parser. None 
                                                          def extract_tables(csv_segment, pdef):
                                                              emitter = Emitter(tables)
                                                              #@inline 9: csv2df.emitter. Emitter.__init__ 
                                                              def __init__(self, tables):
                                                                  self.a = []
                                                                  self.q = []
                                                                  self.m = []
                                                                  for t in tables:
                                                                      self._assert_defined(t)
                                                                      #@inline 10: csv2df.emitter. None 
                                                                      @staticmethod
                                                                          if not table.is_defined():
                                                                          #@inline 11: csv2df.parser. Table.is_defined 
                                                                          def is_defined(self):
                                                                              return bool(self.label and self.splitter_func)
                                                                          #@return: is_defined => True
                                                                      #@return: _assert_defined => None
                                                                      self._import(t)
                                                                      #@inline 10: csv2df.emitter. Emitter._import 
                                                                      def _import(self, table):
                                                                          for row in table.datarows:
                                                                              factory = DatapointMaker(row.get_year(), table.label)
                                                                              #@inline 11: csv2df.reader. Row.get_year 
                                                                              def get_year(self):
                                                                                  return get_year(self.name)
                                                                              #@return: get_year => 2015
                                                                                  #@inline 11: csv2df.emitter. DatapointMaker.__init__ 
                                                                                  def __init__(self, year, label):
                                                                                      self.year = year
                                                                                      self.label = label
                                                                                      self.freq = False
                                                                                      self.value = False
                                                                                      self.period = False
                                                                                  #@return: __init__ => None
                                                                              a_value, q_values, m_values = table.splitter_func(row.data)
                                                                              #@inline 11: csv2df.util_row_splitter. None 
                                                                              def split_row_by_year_and_qtr(row):
                                                                                  return row[0], row[1:1 + 4], None
                                                                              #@return: split_row_by_year_and_qtr => ('83233', ['18568', '19858', '...
                                                                              if a_value:
                                                                                  self.a.append(factory.make('a', a_value))
                                                                                  #@inline 11: csv2df.emitter. DatapointMaker.make 
                                                                                  def make(self, freq: str, x: float, period=False):
                                                                                      self.freq = freq
                                                                                      self.set_value(x)
                                                                                      #@inline 12: csv2df.emitter. DatapointMaker.set_value 
                                                                                      def set_value(self, x):
                                                                                          if x:
                                                                                              self.value = to_float(x)
                                                                                              #@inline 13: csv2df.emitter. None 
                                                                                              def to_float(text: str, i=0):
                                                                                                  i += 1
                                                                                                  if i > 5:
                                                                                                  if not text:
                                                                                                  text = text.replace(",", ".")
                                                                                                  try:
                                                                                                      return float(text)
                                                                                              #@return: to_float => 83233.0
                                                                                      #@return: set_value => None
                                                                                      self.period = period
                                                                                      return self.as_dict()
                                                                                      #@inline 12: csv2df.emitter. DatapointMaker.as_dict 
                                                                                      def as_dict(self):
                                                                                          basedict = dict(year=int(self.year),
                                                                                                          label=self.label,
                                                                                                          freq=self.freq,
                                                                                                          value=self.value,
                                                                                                          time_index=self.get_date())
                                                                                                          #@inline 13: csv2df.emitter. DatapointMaker.get_date 
                                                                                                          def get_date(self):
                                                                                                              if self.freq == 'a':
                                                                                                                  return pd.Timestamp(str(self.year)) + pd.offsets.YearEnd()
                                                                                                          #@return: get_date => 2015-12-31 00:00:00
                                                                                          if self.freq == 'q':
                                                                                          elif self.freq == 'm':
                                                                                          return basedict
                                                                                      #@return: as_dict => {'year': 2015, 'label': 'GDP_b...
                                                                                  #@return: make => {'year': 2015, 'label': 'GDP_b...
                                                                              if q_values:
                                                                                  qs = [factory.make('q', val, t + 1)
                                                                                        for t, val in enumerate(q_values) if val]
                                                                                        #@inline 11: csv2df.emitter. None 
                                                                                        def _import(self, table):
                                                                                            year = int(self.year)
                                                                                            if self.freq == 'q':
                                                                                                month = int(self.period) * 3
                                                                                                base = pd.Timestamp(year, month, 1)
                                                                                                return base + pd.offsets.QuarterEnd()
                                                                                        #@return: get_date => 2015-03-31 00:00:00
                                                                              basedict.update(dict(qtr=self.period))
                                                                                  self.q.extend(qs)
                                                                              if m_values:
                                                                      except ValueError:
                                                                          if " " in text.strip():  # get first value '542,0 5881)'
                                                                          if ")" in text:  # catch '542,01)'
                                                                              match_result = COMMENT_CATCHER.match(text)
                                                                              if match_result:
                                                                                  text = match_result.group(0)
                                                                                  return to_float(text, i)
                                                                      #@return: to_float => 20091.0
                                                              #@return: _import => None
                                                                                  #@inline 9: csv2df.util_row_splitter. None 
                                                                                  def split_row_by_periods(row):
                                                                                      return row[0], row[1:1 + 4], row[1 + 4:1 + 4 + 12]
                                                                                  #@return: split_row_by_periods => ('99,2', ['99,9', '98,3', '99,...
                                                                          ms = [factory.make('m', val, t + 1)
                                                                                for t, val in enumerate(m_values) if val]
                                                                                #@inline 9: csv2df.emitter. None 
                                                                                def _import(self, table):
                                                                                    elif self.freq == 'm':
                                                                                        month = int(self.period)
                                                                                        base = pd.Timestamp(year, month, 1)
                                                                                        return base + pd.offsets.MonthEnd()
                                                                                #@return: get_date => 2015-01-31 00:00:00
                                                                      basedict.update(dict(month=self.period))
                                                                          self.m.extend(ms)
                                                          #@return: __init__ => None
                                                          dfa = emitter.get_dataframe(freq='a')
                                                          #@inline 8: csv2df.emitter. Emitter.get_dataframe 
                                                          def get_dataframe(self, freq):
                                                              df = pd.DataFrame(self._collect(freq)) # TRACE: freq, df.loc[:3]
                                                              #@inline 9: csv2df.emitter. Emitter._collect 
                                                              def _collect(self, freq):
                                                                  if freq in "aqm":
                                                                      return dict(a=self.a, q=self.q, m=self.m)[freq]
                                                              #@return: _collect => [{'year': 2015, 'label': 'GDP_...
                                                              if df.empty:
                                                              self._assert_has_no_duplicate_rows(df)
                                                              #@inline 9: csv2df.emitter. None 
                                                              @staticmethod
                                                                  if df.empty:
                                                                      dups = df[df.duplicated(keep=False)]
                                                                  if not dups.empty:           #
                                                              #@return: _assert_has_no_duplicate_rows => None
                                                              df = df.pivot(columns='label', values='value', index='time_index') # TRACE: df
                                                              df.insert(0, "year", df.index.year)
                                                              if freq == "q":
                                                              elif freq == "m":
                                                              df.columns.name = None
                                                              return df
                                                          #@return: get_dataframe =>             year  GDP_bln_rub ...
                                                          dfq = emitter.get_dataframe(freq='q')
                                                                  df.insert(1, "qtr", df.index.quarter)
                                                          dfm = emitter.get_dataframe(freq='m')
                                                                  df.insert(1, "month", df.index.month)
                                                          return dfa, dfq, dfm
                                                      #@return: get_dataframes => (            year  GDP_bln_rub...
                                                      return dfa1, dfq1, dfm1 
                                                  #@return: test => (            year  GDP_bln_rub...
