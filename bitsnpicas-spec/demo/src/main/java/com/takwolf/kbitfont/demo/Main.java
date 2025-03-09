package com.takwolf.kbitfont.demo;

import com.kreative.bitsnpicas.BitmapFont;
import com.kreative.bitsnpicas.BitmapFontGlyph;
import com.kreative.bitsnpicas.Font;
import com.kreative.bitsnpicas.GlyphPair;
import com.kreative.bitsnpicas.exporter.KbitsBitmapFontExporter;
import com.kreative.bitsnpicas.exporter.KbitxBitmapFontExporter;
import com.kreative.bitsnpicas.importer.KbitsBitmapFontImporter;
import com.kreative.bitsnpicas.importer.KbitxBitmapFontImporter;

import java.io.File;
import java.io.IOException;

public class Main {
    private static final KbitsBitmapFontImporter kbitsImporter = new KbitsBitmapFontImporter();
    private static final KbitsBitmapFontExporter kbitsExporter = new KbitsBitmapFontExporter();

    private static final KbitxBitmapFontImporter kbitxImporter = new KbitxBitmapFontImporter();
    private static final KbitxBitmapFontExporter kbitxExporter = new KbitxBitmapFontExporter();

    private static void convertFonts(File kbitsFile, File kbitxFile) throws IOException {
        BitmapFont font = kbitsImporter.importFont(kbitsFile)[0];
        kbitsExporter.exportFontToFile(font, kbitsFile);
        kbitxExporter.exportFontToFile(font, kbitxFile);
    }

    public static void main(String[] args) throws IOException {
        File testFontsDir = new File("../assets/macintosh");
        convertFonts(new File(testFontsDir, "Athens.kbits"), new File(testFontsDir, "Athens.kbitx"));
        convertFonts(new File(testFontsDir, "Geneva-12.kbits"), new File(testFontsDir, "Geneva-12.kbitx"));
        convertFonts(new File(testFontsDir, "New-York-14.kbits"), new File(testFontsDir, "New-York-14.kbitx"));

        BitmapFont font = new BitmapFont();

        font.setEmAscent(10);
        font.setEmDescent(2);
        font.setLineAscent(10);
        font.setLineDescent(2);
        font.setLineGap(1);
        font.setXHeight(5);
        font.setCapHeight(7);

        font.setName(Font.NAME_FAMILY, "Demo");
        font.setName(Font.NAME_STYLE, "Regular");
        font.setName(Font.NAME_MANUFACTURER, "Made with Bits'n'Picas by Kreative Software");
        font.setName(Font.NAME_DESIGNER, "&'< \"TakWolf\" >'&");
        font.setName(Font.NAME_COPYRIGHT, "Copyright (c) TakWolf");

        byte[][] bitmap = {
                {-1, 50, 50, -1},
                {-1,  0,  0, -1},
                {-1,  0,  0, -1},
                {-1, 25, 25, -1},
        };
        font.putCharacter(0x20, new BitmapFontGlyph(bitmap, 0, 6, 10));
        font.putCharacter(0x21, new BitmapFontGlyph(bitmap, 0, 6, 10));
        font.putNamedGlyph("A", new BitmapFontGlyph(bitmap, 0, 6, 10));
        font.putNamedGlyph("B", new BitmapFontGlyph(bitmap, 0, 6, 10));

        font.setKernPair(new GlyphPair("50", 50), 1);
        font.setKernPair(new GlyphPair(50, "50"), 2);
        font.setKernPair(new GlyphPair("50", "50"), 3);
        font.setKernPair(new GlyphPair(50, 50), 4);

        File demoFontsDir = new File("../assets/demo");
        demoFontsDir.mkdirs();
        kbitsExporter.exportFontToFile(font, new File(demoFontsDir, "demo.kbits"));
        kbitxExporter.exportFontToFile(font, new File(demoFontsDir, "demo.kbitx"));
    }
}
