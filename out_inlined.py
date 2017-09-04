#@inline:
def test():
    dfa1, dfq1, dfm1 = get_dataframes(csvfile1, spec1)
    #@inline:
    def get_dataframes(csvfile, spec=SPEC):
        tables = [t for csv_segment, pdef in Reader(csvfile, spec).items()
        #@inline:
        def __init__(self, csvfile, spec):
            self.rows = list(to_rows(csvfile))
            #@inline:
            def to_rows(csvfile):
                csv_rows = yield_csv_rows(csvfile)
                csv_rows = filter_csv_rows(csv_rows)
                #@inline:
                def filter_csv_rows(gen):
                    filled = filter(lambda row: row and row[0], gen)
                    no_comments = filter(lambda row: not row[0].startswith("___"), filled)
                    return no_comments
                #@inline_end return: filter_csv_rows => <filter object at 0x
                return map(Row, csv_rows)
            #@inline_end return: to_rows => <map object at 0x7fd
                #@inline:
                def yield_csv_rows(csvfile, fmt=CSV_FORMAT):
                    for row in csv.reader(csvfile, **fmt):
                        yield row
                #@inline_end return: yield_csv_rows => []
                        #@inline:
                        filled = filter(lambda row: row and row[0], gen)
                        #@inline:
                        no_comments = filter(lambda row: not row[0].startswith("___"), filled)
                        #@inline:
                        def __init__(self, row):
                            self.name = row[0]
                            self.data = row[1:]
                        #@inline_end return: __init__ => None
                        #@inline_end return: yield_csv_rows => None
                            self.spec = spec
                        #@inline_end return: __init__ => None
                            #@inline:
                            def items(self):
                                rowstack = RowStack(self.rows)
                                #@inline:
                                def __init__(self, rows):
                                    self.rows = list(rows)
                                #@inline_end return: __init__ => None
                                return rowstack.yield_segment_with_defintion(self.spec)
                            #@inline_end return: items => <generator object Ro
                                #@inline:
                                def get_dataframes(csvfile, spec=SPEC):
                                #@inline:
                                def yield_segment_with_defintion(self, spec):
                                    for pdef in spec.get_segment_parsing_definitions():
                                    #@inline:
                                    def get_segment_parsing_definitions(self):
                                        return self.segment_definitions
                                    #@inline_end return: get_segment_parsing_definitions => []
                                    yield self.remaining_rows(), spec.get_main_parsing_definition()
                                    #@inline:
                                    def remaining_rows(self):
                                        remaining = self.rows
                                        self.rows = []
                                        return remaining
                                    #@inline_end return: remaining_rows => [Row(['1. Сводные по
                                        #@inline:
                                        def get_main_parsing_definition(self):
                                            return self.main
                                        #@inline_end return: get_main_parsing_definition => <csv2df.specificatio
                                #@inline_end return: yield_segment_with_defintion => ([Row(['1. Сводные п
                                              for t in extract_tables(csv_segment, pdef)]
                                              #@inline:
                                              def extract_tables(csv_segment, pdef):
                                                  tables = split_to_tables(csv_segment)
                                                  tables = parse_tables(tables, pdef)
                                                  #@inline:
                                                  def parse_tables(tables, pdef):
                                                      tables = [t.set_label(pdef.varnames_dict, pdef.units_dict) for t in tables]
                                                      #@inline:
                                                      def parse_tables(tables, pdef):
                                                      #@inline:
                                                      def split_to_tables(rows):
                                                          datarows = []
                                                          headers = []
                                                          state = State.INIT
                                                          for row in rows:
                                                              if row.is_datarow():
                                                              #@inline:
                                                              def is_datarow(self):
                                                                  return is_year(self.name)
                                                                  #@inline:
                                                                  def is_year(string: str) -> bool:
                                                                      return get_year(string) is not False
                                                                      #@inline:
                                                                      def get_year(string: str, rx=YEAR_CATCHER):
                                                                          match = re.match(rx, string)
                                                                          if match:
                                                                          return False
                                                                      #@inline_end return: get_year => False
                                                                  #@inline_end return: is_year => False
                                                              #@inline_end return: is_datarow => False
                                                                  if state == State.DATA:  # table ended
                                                                  headers.append(row)
                                                                  state = State.UNKNOWN
                                                              year = int(match.group(1))
                                                              if year >= 1991 and year <= 2050:
                                                                  return year
                                                      #@inline_end return: get_year => 2015
                                                                  datarows.append(row)
                                                                  state = State.DATA
                                                                      yield Table(headers, datarows)
                                                                      #@inline:
                                                                      def __init__(self, headers, datarows):
                                                                          self.varname = None
                                                                          self.unit = None
                                                                          self.headers = headers
                                                                          self.lines = odict((row.name, self.UNKNOWN) for row in headers)
                                                                          #@inline:
                                                                          def __init__(self, headers, datarows):
                                                                              self.datarows = datarows
                                                                              self.coln = max(len(row) for row in self.datarows)
                                                                              #@inline:
                                                                              def __init__(self, headers, datarows):
                                                                              #@inline:
                                                                              def __len__(self):
                                                                                  return len(self.data)
                                                                              #@inline_end return: __len__ => 5
                                                                                  self.splitter_func = None
                                                                              #@inline_end return: __init__ => None
                                                                          #@inline_end return: split_to_tables => Table(headers=[Row([
                                                                                  #@inline:
                                                                                  @property
                                                                                      return self.instr.varname_mapper
                                                                                  #@inline_end return: varnames_dict => OrderedDict([('Объем
                                                                                      #@inline:
                                                                                      @property
                                                                                          return self.units
                                                                                      #@inline_end return: units_dict => {'млрд.рублей': 'bln
                                                                                          #@inline:
                                                                                          def set_label(self, varnames_dict, units_dict):
                                                                                              for row in self.headers:
                                                                                                  varname = row.get_varname(varnames_dict)
                                                                                                  #@inline:
                                                                                                  def get_varname(self, varnames_mapper_dict):
                                                                                                      varnames = []
                                                                                                      for k in varnames_mapper_dict.keys():
                                                                                                          if self.matches(k):
                                                                                                          #@inline:
                                                                                                          def matches(self, pat):
                                                                                                              rx = r"\b{}".format(pat)
                                                                                                              return bool(re.search(rx, self.name))
                                                                                                          #@inline_end return: matches => False
                                                                                                      if len(varnames) > 1:
                                                                                                      elif len(varnames) == 1:
                                                                                                          return False
                                                                                                  #@inline_end return: get_varname => False
                                                                                                  if varname:
                                                                                                  unit = row.get_unit(units_dict)
                                                                                                  #@inline:
                                                                                                  def get_unit(self, units_mapper_dict):
                                                                                                      for k in units_mapper_dict.keys():
                                                                                                          if k in self.name:
                                                                                                      return False
                                                                                                  #@inline_end return: get_unit => False
                                                                                                  if unit:
                                                                                                      varnames.append(varnames_mapper_dict[k])
                                                                                                  return varnames[0]
                                                                                          #@inline_end return: get_varname => 'GDP'
                                                                                  self.varname = varname
                                                                                  self.lines[row.name] = self.KNOWN
                                                                                  return units_mapper_dict[k]
                                                                      #@inline_end return: get_unit => 'bln_rub'
                                                                      self.unit = unit
                                                                      self.lines[row.name] = self.KNOWN
                                                              return self
                                                      #@inline_end return: set_label => Table(headers=[Row([
                                                                  headers = []
                                                                  datarows = []
                                                      if len(headers) > 0 and len(datarows) > 0:
                                                  #@inline_end return: split_to_tables => None
                                                  tables = [t.set_splitter(pdef.funcname) for t in tables]
                                                  #@inline:
                                                  def parse_tables(tables, pdef):
                                                  #@inline:
                                                  @property
                                                      return self.reader
                                                  #@inline_end return: funcname => False
                                                      #@inline:
                                                      def set_splitter(self, funcname):
                                                          self.splitter_func = splitter.get_splitter(funcname or self.coln)
                                                          #@inline:
                                                          def get_splitter(arg):
                                                              try:
                                                                  return FUNC_MAPPER[arg]
                                                          #@inline_end return: get_splitter => <function split_row_
                                                          return self
                                                      #@inline_end return: set_splitter => Table(headers=[Row([
                                                      def fix_multitable_units(tables):
                                                      fix_multitable_units(tables)
                                                      #@inline:
                                                      def fix_multitable_units(tables):
                                                          for prev_table, table in zip(tables, tables[1:]):
                                                              if table.varname is None and not table.has_unknown_lines():
                                                              #@inline:
                                                              def has_unknown_lines(self):
                                                                  return self.UNKNOWN in self.lines.values()
                                                              #@inline_end return: has_unknown_lines => False
                                                                  table.varname = prev_table.varname
                                                      #@inline_end return: fix_multitable_units => None
                                                      return tables
                                                  #@inline_end return: parse_tables => [Table(headers=[Row(
                                                  verify_tables(tables, pdef)
                                                  #@inline:
                                                  def verify_tables(tables, pdef):
                                                      _labels_in_tables = [t.label for t in tables]
                                                      #@inline:
                                                      def verify_tables(tables, pdef):
                                                      #@inline:
                                                      @property
                                                          vn = self.varname
                                                          u = self.unit
                                                          if vn and u:
                                                              return make_label(vn, u)
                                                              #@inline:
                                                              def make_label(vn, unit, sep=SEP):
                                                                  return vn + sep + unit
                                                              #@inline_end return: make_label => 'GDP_bln_rub'
                                                      #@inline_end return: label => 'GDP_bln_rub'
                                                          _labels_missed = [x for x in pdef.required if x not in _labels_in_tables]
                                                          #@inline:
                                                          @property
                                                              return self.instr.required_labels
                                                          #@inline_end return: required => ['GDP_bln_rub', 'IND
                                                              #@inline:
                                                              def verify_tables(tables, pdef):
                                                                  if _labels_missed:
                                                              #@inline_end return: verify_tables => None
                                                          return [t for t in tables if t.label in pdef.required]
                                                          #@inline:
                                                          def extract_tables(csv_segment, pdef):
                                                              emitter = Emitter(tables)
                                                              #@inline:
                                                              def __init__(self, tables):
                                                                  self.a = []
                                                                  self.q = []
                                                                  self.m = []
                                                                  for t in tables:
                                                                      self._assert_defined(t)
                                                                      #@inline:
                                                                      @staticmethod
                                                                          if not table.is_defined():
                                                                          #@inline:
                                                                          def is_defined(self):
                                                                              return bool(self.label and self.splitter_func)
                                                                          #@inline_end return: is_defined => True
                                                                      #@inline_end return: _assert_defined => None
                                                                      self._import(t)
                                                                      #@inline:
                                                                      def _import(self, table):
                                                                          for row in table.datarows:
                                                                              factory = DatapointMaker(row.get_year(), table.label)
                                                                              #@inline:
                                                                              def get_year(self):
                                                                                  return get_year(self.name)
                                                                              #@inline_end return: get_year => 2015
                                                                                  #@inline:
                                                                                  def __init__(self, year, label):
                                                                                      self.year = year
                                                                                      self.label = label
                                                                                      self.freq = False
                                                                                      self.value = False
                                                                                      self.period = False
                                                                                  #@inline_end return: __init__ => None
                                                                              a_value, q_values, m_values = table.splitter_func(row.data)
                                                                              #@inline:
                                                                              def split_row_by_year_and_qtr(row):
                                                                                  return row[0], row[1:1 + 4], None
                                                                              #@inline_end return: split_row_by_year_and_qtr => ('83233', ['18568', 
                                                                              if a_value:
                                                                                  self.a.append(factory.make('a', a_value))
                                                                                  #@inline:
                                                                                  def make(self, freq: str, x: float, period=False):
                                                                                      self.freq = freq
                                                                                      self.set_value(x)
                                                                                      #@inline:
                                                                                      def set_value(self, x):
                                                                                          if x:
                                                                                              self.value = to_float(x)
                                                                                              #@inline:
                                                                                              def to_float(text: str, i=0):
                                                                                                  i += 1
                                                                                                  if i > 5:
                                                                                                  if not text:
                                                                                                  text = text.replace(",", ".")
                                                                                                  try:
                                                                                                      return float(text)
                                                                                              #@inline_end return: to_float => 83233.0
                                                                                      #@inline_end return: set_value => None
                                                                                      self.period = period
                                                                                      return self.as_dict()
                                                                                      #@inline:
                                                                                      def as_dict(self):
                                                                                          basedict = dict(year=int(self.year),
                                                                                                          label=self.label,
                                                                                                          freq=self.freq,
                                                                                                          value=self.value,
                                                                                                          time_index=self.get_date())
                                                                                                          #@inline:
                                                                                                          def get_date(self):
                                                                                                              if self.freq == 'a':
                                                                                                                  return pd.Timestamp(str(self.year)) + pd.offsets.YearEnd()
                                                                                                          #@inline_end return: get_date => Timestamp('2015-12-3
                                                                                          if self.freq == 'q':
                                                                                          elif self.freq == 'm':
                                                                                          return basedict
                                                                                      #@inline_end return: as_dict => {'year': 2015, 'labe
                                                                                  #@inline_end return: make => {'year': 2015, 'labe
                                                                              if q_values:
                                                                                  qs = [factory.make('q', val, t + 1)
                                                                                        for t, val in enumerate(q_values) if val]
                                                                                        #@inline:
                                                                                        def _import(self, table):
                                                                                            year = int(self.year)
                                                                                            if self.freq == 'q':
                                                                                                month = int(self.period) * 3
                                                                                                base = pd.Timestamp(year, month, 1)
                                                                                                return base + pd.offsets.QuarterEnd()
                                                                                        #@inline_end return: get_date => Timestamp('2015-03-3
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
                                                                      #@inline_end return: to_float => 20091.0
                                                              #@inline_end return: _import => None
                                                                                  #@inline:
                                                                                  def split_row_by_periods(row):
                                                                                      return row[0], row[1:1 + 4], row[1 + 4:1 + 4 + 12]
                                                                                  #@inline_end return: split_row_by_periods => ('99,2', ['99,9', '9
                                                                          ms = [factory.make('m', val, t + 1)
                                                                                for t, val in enumerate(m_values) if val]
                                                                                #@inline:
                                                                                def _import(self, table):
                                                                                    elif self.freq == 'm':
                                                                                        month = int(self.period)
                                                                                        base = pd.Timestamp(year, month, 1)
                                                                                        return base + pd.offsets.MonthEnd()
                                                                                #@inline_end return: get_date => Timestamp('2015-01-3
                                                                      basedict.update(dict(month=self.period))
                                                                          self.m.extend(ms)
                                                          #@inline_end return: __init__ => None
                                                          dfa = emitter.get_dataframe(freq='a')
                                                          #@inline:
                                                          def get_dataframe(self, freq):
                                                              df = pd.DataFrame(self._collect(freq)) # TRACE: freq, df.loc[:3]
                                                              #@inline:
                                                              def _collect(self, freq):
                                                                  if freq in "aqm":
                                                                      return dict(a=self.a, q=self.q, m=self.m)[freq]
                                                              #@inline_end return: _collect => [{'year': 2015, 'lab
                                                              if df.empty:
                                                              self._assert_has_no_duplicate_rows(df)
                                                              #@inline:
                                                              @staticmethod
                                                                  if df.empty:
                                                                      dups = df[df.duplicated(keep=False)]
                                                                  if not dups.empty:           #
                                                              #@inline_end return: _assert_has_no_duplicate_rows => None
                                                              df = df.pivot(columns='label', values='value', index='time_index') # TRACE: df
                                                              df.insert(0, "year", df.index.year)
                                                              if freq == "q":
                                                              elif freq == "m":
                                                              df.columns.name = None
                                                              return df
                                                          #@inline_end return: get_dataframe =>             year  GD
                                                          dfq = emitter.get_dataframe(freq='q')
                                                                  df.insert(1, "qtr", df.index.quarter)
                                                          dfm = emitter.get_dataframe(freq='m')
                                                                  df.insert(1, "month", df.index.month)
                                                          return dfa, dfq, dfm
                                                      #@inline_end return: get_dataframes => (            year  G
                                                      return dfa1, dfq1, dfm1 
                                                  #@inline_end return: test => (            year  G
