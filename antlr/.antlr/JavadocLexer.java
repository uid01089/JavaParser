// Generated from /home/konrad/Dokumente/Python/JavaReader/JavaParser/antlr/JavadocLexer.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class JavadocLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		NAME=1, NEWLINE=2, SPACE=3, TEXT_CONTENT=4, AT=5, STAR=6, SLASH=7, JAVADOC_START=8, 
		JAVADOC_END=9, INLINE_TAG_START=10, BRACE_OPEN=11, BRACE_CLOSE=12;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"NAME", "NEWLINE", "SPACE", "TEXT_CONTENT", "AT", "STAR", "SLASH", "JAVADOC_START", 
			"JAVADOC_END", "INLINE_TAG_START", "BRACE_OPEN", "BRACE_CLOSE"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, null, "'@'", "'*'", "'/'", null, null, "'{@'", 
			"'{'", "'}'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "NAME", "NEWLINE", "SPACE", "TEXT_CONTENT", "AT", "STAR", "SLASH", 
			"JAVADOC_START", "JAVADOC_END", "INLINE_TAG_START", "BRACE_OPEN", "BRACE_CLOSE"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public JavadocLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "JavadocLexer.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	@Override
	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 1:
			return NEWLINE_sempred((RuleContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean NEWLINE_sempred(RuleContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return _input.LA(1) != '/';
		case 1:
			return _input.LA(1) != '/';
		case 2:
			return _input.LA(1) != '/';
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0000\fy\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0001\u0000\u0004\u0000\u001b\b\u0000\u000b\u0000\f\u0000"+
		"\u001c\u0001\u0001\u0001\u0001\u0003\u0001!\b\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0004\u0001&\b\u0001\u000b\u0001\f\u0001\'\u0003\u0001"+
		"*\b\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001"+
		"0\b\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0004\u00015\b\u0001\u000b"+
		"\u0001\f\u00016\u0003\u00019\b\u0001\u0001\u0001\u0001\u0001\u0003\u0001"+
		"=\b\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0004\u0001B\b\u0001\u000b"+
		"\u0001\f\u0001C\u0003\u0001F\b\u0001\u0003\u0001H\b\u0001\u0001\u0002"+
		"\u0004\u0002K\b\u0002\u000b\u0002\f\u0002L\u0001\u0003\u0004\u0003P\b"+
		"\u0003\u000b\u0003\f\u0003Q\u0001\u0004\u0001\u0004\u0001\u0005\u0001"+
		"\u0005\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0005\u0007_\b\u0007\n\u0007\f\u0007b\t\u0007\u0001"+
		"\b\u0003\be\b\b\u0001\b\u0003\bh\b\b\u0001\b\u0005\bk\b\b\n\b\f\bn\t\b"+
		"\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001"+
		"\u000b\u0001\u000b\u0000\u0000\f\u0001\u0001\u0003\u0002\u0005\u0003\u0007"+
		"\u0004\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b"+
		"\u0017\f\u0001\u0000\u0004\u0002\u0000AZaz\u0002\u0000\t\t  \b\u0000\t"+
		"\n\r\r  **//@Za{}}\u0002\u0000\n\n\r\r\u008a\u0000\u0001\u0001\u0000\u0000"+
		"\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000"+
		"\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000"+
		"\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000"+
		"\u000f\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000\u0000"+
		"\u0013\u0001\u0000\u0000\u0000\u0000\u0015\u0001\u0000\u0000\u0000\u0000"+
		"\u0017\u0001\u0000\u0000\u0000\u0001\u001a\u0001\u0000\u0000\u0000\u0003"+
		"G\u0001\u0000\u0000\u0000\u0005J\u0001\u0000\u0000\u0000\u0007O\u0001"+
		"\u0000\u0000\u0000\tS\u0001\u0000\u0000\u0000\u000bU\u0001\u0000\u0000"+
		"\u0000\rW\u0001\u0000\u0000\u0000\u000fY\u0001\u0000\u0000\u0000\u0011"+
		"d\u0001\u0000\u0000\u0000\u0013r\u0001\u0000\u0000\u0000\u0015u\u0001"+
		"\u0000\u0000\u0000\u0017w\u0001\u0000\u0000\u0000\u0019\u001b\u0007\u0000"+
		"\u0000\u0000\u001a\u0019\u0001\u0000\u0000\u0000\u001b\u001c\u0001\u0000"+
		"\u0000\u0000\u001c\u001a\u0001\u0000\u0000\u0000\u001c\u001d\u0001\u0000"+
		"\u0000\u0000\u001d\u0002\u0001\u0000\u0000\u0000\u001e)\u0005\n\u0000"+
		"\u0000\u001f!\u0003\u0005\u0002\u0000 \u001f\u0001\u0000\u0000\u0000 "+
		"!\u0001\u0000\u0000\u0000!%\u0001\u0000\u0000\u0000\"#\u0003\u000b\u0005"+
		"\u0000#$\u0004\u0001\u0000\u0000$&\u0001\u0000\u0000\u0000%\"\u0001\u0000"+
		"\u0000\u0000&\'\u0001\u0000\u0000\u0000\'%\u0001\u0000\u0000\u0000\'("+
		"\u0001\u0000\u0000\u0000(*\u0001\u0000\u0000\u0000) \u0001\u0000\u0000"+
		"\u0000)*\u0001\u0000\u0000\u0000*H\u0001\u0000\u0000\u0000+,\u0005\r\u0000"+
		"\u0000,-\u0005\n\u0000\u0000-8\u0001\u0000\u0000\u0000.0\u0003\u0005\u0002"+
		"\u0000/.\u0001\u0000\u0000\u0000/0\u0001\u0000\u0000\u000004\u0001\u0000"+
		"\u0000\u000012\u0003\u000b\u0005\u000023\u0004\u0001\u0001\u000035\u0001"+
		"\u0000\u0000\u000041\u0001\u0000\u0000\u000056\u0001\u0000\u0000\u0000"+
		"64\u0001\u0000\u0000\u000067\u0001\u0000\u0000\u000079\u0001\u0000\u0000"+
		"\u00008/\u0001\u0000\u0000\u000089\u0001\u0000\u0000\u00009H\u0001\u0000"+
		"\u0000\u0000:E\u0005\r\u0000\u0000;=\u0003\u0005\u0002\u0000<;\u0001\u0000"+
		"\u0000\u0000<=\u0001\u0000\u0000\u0000=A\u0001\u0000\u0000\u0000>?\u0003"+
		"\u000b\u0005\u0000?@\u0004\u0001\u0002\u0000@B\u0001\u0000\u0000\u0000"+
		"A>\u0001\u0000\u0000\u0000BC\u0001\u0000\u0000\u0000CA\u0001\u0000\u0000"+
		"\u0000CD\u0001\u0000\u0000\u0000DF\u0001\u0000\u0000\u0000E<\u0001\u0000"+
		"\u0000\u0000EF\u0001\u0000\u0000\u0000FH\u0001\u0000\u0000\u0000G\u001e"+
		"\u0001\u0000\u0000\u0000G+\u0001\u0000\u0000\u0000G:\u0001\u0000\u0000"+
		"\u0000H\u0004\u0001\u0000\u0000\u0000IK\u0007\u0001\u0000\u0000JI\u0001"+
		"\u0000\u0000\u0000KL\u0001\u0000\u0000\u0000LJ\u0001\u0000\u0000\u0000"+
		"LM\u0001\u0000\u0000\u0000M\u0006\u0001\u0000\u0000\u0000NP\b\u0002\u0000"+
		"\u0000ON\u0001\u0000\u0000\u0000PQ\u0001\u0000\u0000\u0000QO\u0001\u0000"+
		"\u0000\u0000QR\u0001\u0000\u0000\u0000R\b\u0001\u0000\u0000\u0000ST\u0005"+
		"@\u0000\u0000T\n\u0001\u0000\u0000\u0000UV\u0005*\u0000\u0000V\f\u0001"+
		"\u0000\u0000\u0000WX\u0005/\u0000\u0000X\u000e\u0001\u0000\u0000\u0000"+
		"YZ\u0005/\u0000\u0000Z[\u0005*\u0000\u0000[\\\u0005*\u0000\u0000\\`\u0001"+
		"\u0000\u0000\u0000]_\u0003\u000b\u0005\u0000^]\u0001\u0000\u0000\u0000"+
		"_b\u0001\u0000\u0000\u0000`^\u0001\u0000\u0000\u0000`a\u0001\u0000\u0000"+
		"\u0000a\u0010\u0001\u0000\u0000\u0000b`\u0001\u0000\u0000\u0000ce\u0007"+
		"\u0003\u0000\u0000dc\u0001\u0000\u0000\u0000de\u0001\u0000\u0000\u0000"+
		"eg\u0001\u0000\u0000\u0000fh\u0003\u0005\u0002\u0000gf\u0001\u0000\u0000"+
		"\u0000gh\u0001\u0000\u0000\u0000hl\u0001\u0000\u0000\u0000ik\u0003\u000b"+
		"\u0005\u0000ji\u0001\u0000\u0000\u0000kn\u0001\u0000\u0000\u0000lj\u0001"+
		"\u0000\u0000\u0000lm\u0001\u0000\u0000\u0000mo\u0001\u0000\u0000\u0000"+
		"nl\u0001\u0000\u0000\u0000op\u0005*\u0000\u0000pq\u0005/\u0000\u0000q"+
		"\u0012\u0001\u0000\u0000\u0000rs\u0005{\u0000\u0000st\u0005@\u0000\u0000"+
		"t\u0014\u0001\u0000\u0000\u0000uv\u0005{\u0000\u0000v\u0016\u0001\u0000"+
		"\u0000\u0000wx\u0005}\u0000\u0000x\u0018\u0001\u0000\u0000\u0000\u0012"+
		"\u0000\u001c \')/68<CEGLQ`dgl\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}