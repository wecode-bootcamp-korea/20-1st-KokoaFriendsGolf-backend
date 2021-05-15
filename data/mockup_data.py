USER_NUMBER      = 100
NEW_RATE         = 0.05
SALE_RATE        = 0.1
SOLDOUT_RATE     = 0.03
SET_RATE         = 0.01
PICKED_RATE      = 0.05
PRICE_VOLATILITY = 0.03

CHARACTERS = [
    {"id": 1, "name": "콘콘", "url": "https://i.ibb.co/Y26pvpF/dinosaur.png"},
    {"id": 2, "name": "춘삼이", "url": "https://i.ibb.co/vwVTZP5/trunk.png"},
    {"id": 3, "name": "삐약이", "url": "https://i.ibb.co/WPmLcVf/bird.png"},
    {"id": 4, "name": "피치피치", "url": "https://i.ibb.co/BC7XQvW/peach.png"},
    {"id": 5, "name": "덕이", "url": "https://i.ibb.co/1mNL56P/ducky.png"},
]

CATEGORY = [
    {
        "id"         : 1,
        "name"       : "일렉트로닉",
        "subcategory": [
            {
                "id"       : 1,
                "name"     : "아이맥",
                "avg_price": 3_000_000
            },
            {
                "id"       : 2,
                "name"     : "태블릿",
                "avg_price": 1_500_000
            },
            {
                "id"       : 3,
                "name"     : "폰",
                "avg_price": 1_000_000
            },
            {
                "id"       : 4,
                "name"     : "워치",
                "avg_price": 500_000
            },
        ]
    },    
    {
        "id"         : 2,
        "name"       : "웨어",
        "subcategory": [
            {
                "id"       : 1,
                "name"     : "셔츠",
                "avg_price": 50000
            },
            {
                "id"       : 2,
                "name"     : "모자",
                "avg_price": 30000
            },
            {
                "id"       : 3,
                "name"     : "후드",
                "avg_price": 50000,
            },
        ]
    },    
    {
        "id"         : 3,
        "name"       : "리빙",
        "subcategory": [
            {
                "id"       : 1,
                "name"     : "컵",
                "avg_price": 10000
            },
            {
                "id"       : 2,
                "name"     : "책",
                "avg_price": 15000
            },
        ]
    },    
]

PRODUCT_NAME_PREFIX = [
    "베이직",
    "렛츠파티",
    "프렌즈",
    "썸머 씨즌",
    "소프트",
    "윈터랜드",
    "고오급",
    "신상",
    "2021 NEW",
    "시즌한정",
    "리미티드",
    "기간한정",
    "20대 추천 상품",
    "막강",
    "스테디셀러",
    "베스트",
    "이탈리아 장인이 만든",
    "로켓배송",
    "당일배송",
    "스위스 직수입",
    "아이가 너무 좋아하는",
    "20대 생일선물용",
    "수고한 당신에게",
]

ENG_KO = {
    "Electronics": "일렉트로닉",
    "Living"     : "리빙",
    "Wear"       : "웨어",
    "Imac"       : "아이맥",
    "Cup"        : "컵",
    "Hoodie"     : "후드",
    "Caps"       : "모자",
    "Books"      : "책",
    "Shirts"     : "셔츠",
    "Tablet"     : "태블릿",
    "Watch"      : "워치",
    "Phone"      : "폰",
    "Chunsam"    : "춘삼이",
    "Peach"      : "피치피치",
    "Duckee"     : "덕이",
    "Concon"     : "콘콘",
    "Peepee"     : "삐약이",
}

PRODUCT_IMAGES = [
    "https://i.ibb.co/VtMY3gh/Electronics-Imac-Chunsam-0.png",
    "https://i.ibb.co/6JDgQZQ/Electronics-Imac-Chunsam-1.png",
    "https://i.ibb.co/2qMJ9kd/Electronics-Imac-Chunsam-2.png",
    "https://i.ibb.co/R2ZWqpZ/Electronics-Imac-Chunsam-3.png",
    "https://i.ibb.co/MkyYDgF/Electronics-Imac-Chunsam-4.png",
    "https://i.ibb.co/fnhppMJ/Electronics-Imac-Concon-0.png",
    "https://i.ibb.co/zrrbfgW/Electronics-Imac-Concon-1.png",
    "https://i.ibb.co/1YgrK6H/Electronics-Imac-Concon-3.png",
    "https://i.ibb.co/Qp5k2bL/Electronics-Imac-Duckee-0.png",
    "https://i.ibb.co/Hz8RQfK/Electronics-Imac-Duckee-1.png",
    "https://i.ibb.co/9rQFFN0/Electronics-Imac-Duckee-2.png",
    "https://i.ibb.co/sJLRRX6/Electronics-Imac-Duckee-3.png",
    "https://i.ibb.co/p0fcznL/Electronics-Imac-Duckee-4.png",
    "https://i.ibb.co/x5BdJz7/Electronics-Imac-Duckee-5.png",
    "https://i.ibb.co/ZWPsXDw/Electronics-Imac-Duckee-6.png",
    "https://i.ibb.co/sJLRRX6/Electronics-Imac-Duckee-3.png",
    "https://i.ibb.co/WssQ3Rh/Electronics-Imac-Peach-0.png",
    "https://i.ibb.co/P5MHYYJ/Electronics-Imac-Peach-1.png",
    "https://i.ibb.co/vzrrwgB/Electronics-Imac-Peach-2.png",
    "https://i.ibb.co/KKhX8rk/Electronics-Imac-Peach-3.png",
    "https://i.ibb.co/sJNkqp4/Electronics-Imac-Peach-4.png",
    "https://i.ibb.co/XXbfKFP/Electronics-Imac-Peach-5.png",
    "https://i.ibb.co/7ghRSXB/Electronics-Imac-Peach-6.png",
    "https://i.ibb.co/RjNj7vn/Electronics-Imac-Peach-7.png",
    "https://i.ibb.co/RzZ7y97/Electronics-Imac-Peach-8.png",
    "https://i.ibb.co/PQKSs41/Electronics-Imac-Peepee-0.png",
    "https://i.ibb.co/YTKnZcg/Electronics-Imac-Peepee-1.png",
    "https://i.ibb.co/4pQyBj3/Electronics-Imac-Peepee-2.png",
    "https://i.ibb.co/yYbVZ6G/Electronics-Imac-Peepee-3.png",
    "https://i.ibb.co/vz9kG8m/Electronics-Imac-Peepee-4.png",
    "https://i.ibb.co/crWMkYs/Electronics-Imac-Peepee-5.png",
    "https://i.ibb.co/YTKnZcg/Electronics-Imac-Peepee-1.png",
    "https://i.ibb.co/JBHb14W/Electronics-Imac-Peepee-7.png",
    "https://i.ibb.co/PDfLdWt/Electronics-Imac-Peepee-8.png",
    "https://i.ibb.co/y4QW9bL/Electronics-Imac-Peepee-9.png",
    "https://i.ibb.co/pbPjH20/Electronics-Phone-Chunsam-0.png",
    "https://i.ibb.co/ysSw9br/Electronics-Phone-Chunsam-2.png",
    "https://i.ibb.co/N6mNnv1/Electronics-Phone-Chunsam-3.png",
    "https://i.ibb.co/DGZKX7f/Electronics-Phone-Chunsam-4.png",
    "https://i.ibb.co/XxgDs6T/Electronics-Phone-Chunsam-5.png",
    "https://i.ibb.co/5903SVW/Electronics-Phone-Concon-0.png",
    "https://i.ibb.co/0fqcf62/Electronics-Phone-Concon-1.png",
    "https://i.ibb.co/b6yqdzk/Electronics-Phone-Concon-2.png",
    "https://i.ibb.co/xzRThHL/Electronics-Phone-Concon-5.png",
    "https://i.ibb.co/8Y5SgQ6/Electronics-Phone-Concon-6.png",
    "https://i.ibb.co/hMrt8rX/Electronics-Phone-Duckee-0.png",
    "https://i.ibb.co/fktfFTp/Electronics-Phone-Duckee-1.png",
    "https://i.ibb.co/kg3csBR/Electronics-Phone-Duckee-2.png",
    "https://i.ibb.co/1Rg8X5M/Electronics-Phone-Duckee-3.png",
    "https://i.ibb.co/1JrPt3g/Electronics-Phone-Duckee-4.png",
    "https://i.ibb.co/kmQ1ThC/Electronics-Phone-Duckee-6.png",
    "https://i.ibb.co/jWHgfQp/Electronics-Phone-Peach-0.png",
    "https://i.ibb.co/PNNnYFj/Electronics-Phone-Peach-1.png",
    "https://i.ibb.co/bsVyJqb/Electronics-Phone-Peach-2.png",
    "https://i.ibb.co/yN258Vb/Electronics-Phone-Peach-3.png",
    "https://i.ibb.co/BKMwnyT/Electronics-Phone-Peach-4.png",
    "https://i.ibb.co/mJSnrp3/Electronics-Phone-Peach-6.png",
    "https://i.ibb.co/KK2vjXN/Electronics-Phone-Peepee-0.png",
    "https://i.ibb.co/s2Mg3gB/Electronics-Phone-Peepee-1.png",
    "https://i.ibb.co/SXCJGZb/Electronics-Phone-Peepee-3.png",
    "https://i.ibb.co/n7cYbbC/Electronics-Phone-Peepee-4.png",
    "https://i.ibb.co/fv4pKJr/Electronics-Phone-Peepee-5.png",
    "https://i.ibb.co/L6R288P/Electronics-Tablet-Chunsam-0.png",
    "https://i.ibb.co/LxJ97vW/Electronics-Tablet-Chunsam-1.png",
    "https://i.ibb.co/hV3CDMY/Electronics-Tablet-Chunsam-2.png",
    "https://i.ibb.co/FbfMqJR/Electronics-Tablet-Chunsam-3.png",
    "https://i.ibb.co/gVDHpTS/Electronics-Tablet-Concon-0.png",
    "https://i.ibb.co/sbcp9Z5/Electronics-Tablet-Concon-1.png",
    "https://i.ibb.co/19hMyfN/Electronics-Tablet-Concon-3.png",
    "https://i.ibb.co/yQywfNn/Electronics-Tablet-Concon-4.png",
    "https://i.ibb.co/VM9hxqX/Electronics-Tablet-Concon-5.png",
    "https://i.ibb.co/KbxVGb7/Electronics-Tablet-Concon-6.png",
    "https://i.ibb.co/tDWDwR5/Electronics-Tablet-Duckee-0.png",
    "https://i.ibb.co/pJyDBNg/Electronics-Tablet-Duckee-1.png",
    "https://i.ibb.co/TK4mRSM/Electronics-Tablet-Duckee-2.png",
    "https://i.ibb.co/3FRskBJ/Electronics-Tablet-Duckee-3.png",
    "https://i.ibb.co/mRM48Bs/Electronics-Tablet-Peach-0.png",
    "https://i.ibb.co/Sc5wGxV/Electronics-Tablet-Peach-1.png",
    "https://i.ibb.co/2kBjQtn/Electronics-Tablet-Peach-2.png",
    "https://i.ibb.co/3FdPNQW/Electronics-Tablet-Peepee-0.png",
    "https://i.ibb.co/0yGr9kB/Electronics-Tablet-Peepee-1.png",
    "https://i.ibb.co/3YfVx91/Electronics-Tablet-Peepee-2.png",
    "https://i.ibb.co/Mf37XXc/Electronics-Tablet-Peepee-3.png",
    "https://i.ibb.co/rx1mC8Q/Electronics-Watch-Chunsam-0.png",
    "https://i.ibb.co/DCTxRXH/Electronics-Watch-Chunsam-1.png",
    "https://i.ibb.co/5kzZNQ6/Electronics-Watch-Chunsam-2.png",
    "https://i.ibb.co/WPbS19G/Electronics-Watch-Chunsam-3.png",
    "https://i.ibb.co/W0X1Y8T/Electronics-Watch-Chunsam-4.png",
    "https://i.ibb.co/8bTjMRC/Electronics-Watch-Concon-1.png",
    "https://i.ibb.co/p2D4zdc/Electronics-Watch-Concon-2.png",
    "https://i.ibb.co/MSMNV3q/Electronics-Watch-Concon-3.png",
    "https://i.ibb.co/1Ry4JH7/Electronics-Watch-Concon-4.png",
    "https://i.ibb.co/CtqQ05j/Electronics-Watch-Concon-5.png",
    "https://i.ibb.co/QFppTgf/Electronics-Watch-Duckee-0.png",
    "https://i.ibb.co/NVw6y5w/Electronics-Watch-Duckee-1.png",
    "https://i.ibb.co/HDm5Wd7/Electronics-Watch-Duckee-2.png",
    "https://i.ibb.co/QDQ56LM/Electronics-Watch-Duckee-3.png",
    "https://i.ibb.co/S0zDyD7/Electronics-Watch-Duckee-4.png",
    "https://i.ibb.co/YRKRRLk/Electronics-Watch-Peach-0.png",
    "https://i.ibb.co/QHSzkvB/Electronics-Watch-Peach-1.png",
    "https://i.ibb.co/TMsmMxf/Electronics-Watch-Peach-2.png",
    "https://i.ibb.co/1M3XBmh/Electronics-Watch-Peach-3.png",
    "https://i.ibb.co/dPScsdY/Electronics-Watch-Peach-4.png",
    "https://i.ibb.co/1M3XBmh/Electronics-Watch-Peach-3.png",
    "https://i.ibb.co/bXpkgmN/Electronics-Watch-Peach-6.png",
    "https://i.ibb.co/VTJgCzX/Electronics-Watch-Peepee-0.png",
    "https://i.ibb.co/rdhR55B/Electronics-Watch-Peepee-1.png",
    "https://i.ibb.co/X243SPn/Electronics-Watch-Peepee-2.png",
    "https://i.ibb.co/jrgs80P/Electronics-Watch-Peepee-3.png",
    "https://i.ibb.co/X2nHg3M/Electronics-Watch-Peepee-4.png",
    "https://i.ibb.co/qrtk30X/Electronics-Watch-Peepee-5.png",
    "https://i.ibb.co/g785DDF/Living-Books-Chunsam-0.png",
    "https://i.ibb.co/KDSfn38/Living-Books-Chunsam-1.png",
    "https://i.ibb.co/QXFXhKh/Living-Books-Chunsam-2.png",
    "https://i.ibb.co/fFgvcj2/Living-Books-Chunsam-3.png",
    "https://i.ibb.co/bvmx4jB/Living-Books-Concon-0.png",
    "https://i.ibb.co/KGn42Jn/Living-Books-Concon-2.png",
    "https://i.ibb.co/2WyjXRW/Living-Books-Concon-3.png",
    "https://i.ibb.co/pWbzRJk/Living-Books-Concon-4.png",
    "https://i.ibb.co/xzSY3Mr/Living-Books-Concon-5.png",
    "https://i.ibb.co/FW27hsr/Living-Books-Duckee-0.png",
    "https://i.ibb.co/TrbD93j/Living-Books-Duckee-1.png",
    "https://i.ibb.co/55PQp9V/Living-Books-Duckee-4.png",
    "https://i.ibb.co/z2mHRHz/Living-Books-Peach-0.png",
    "https://i.ibb.co/sQHF6wh/Living-Books-Peach-1.png",
    "https://i.ibb.co/W0p5f0j/Living-Books-Peach-2.png",
    "https://i.ibb.co/W6jnkjW/Living-Books-Peach-3.png",
    "https://i.ibb.co/H24Nkry/Living-Books-Peach-4.png",
    "https://i.ibb.co/NtFxZ0r/Living-Books-Peepee-0.png",
    "https://i.ibb.co/HVL4BxK/Living-Books-Peepee-1.png",
    "https://i.ibb.co/M9qcJx9/Living-Books-Peepee-2.png",
    "https://i.ibb.co/ChCsPYy/Living-Books-Peepee-3.png",
    "https://i.ibb.co/QN60KGr/Living-Books-Peepee-4.png",
    "https://i.ibb.co/805KwsP/Living-Cup-Chunsam-0.png",
    "https://i.ibb.co/19qM7g1/Living-Cup-Chunsam-1.png",
    "https://i.ibb.co/9qVFBfs/Living-Cup-Chunsam-2.png",
    "https://i.ibb.co/rHhrtHb/Living-Cup-Concon-1.png",
    "https://i.ibb.co/rMpR3t5/Living-Cup-Concon-2.png",
    "https://i.ibb.co/YTG7hx1/Living-Cup-Duckee-0.png",
    "https://i.ibb.co/tD02SvN/Living-Cup-Duckee-1.png",
    "https://i.ibb.co/BCnv7tX/Living-Cup-Duckee-2.png",
    "https://i.ibb.co/4gsyXbQ/Living-Cup-Duckee-3.png",
    "https://i.ibb.co/7Gb4kyQ/Living-Cup-Peach-0.png",
    "https://i.ibb.co/PgGvT8J/Living-Cup-Peach-1.png",
    "https://i.ibb.co/51jQZ8W/Living-Cup-Peepee-0.png",
    "https://i.ibb.co/j8CfqX0/Living-Cup-Peepee-1.png",
    "https://i.ibb.co/ZMLfTtF/Living-Cup-Peepee-2.png",
    "https://i.ibb.co/bJKTL28/Wear-Caps-Chunsam-0.png",
    "https://i.ibb.co/BV14HQh/Wear-Caps-Chunsam-1.png",
    "https://i.ibb.co/KLVCsCx/Wear-Caps-Chunsam-2.png",
    "https://i.ibb.co/mc0mjc8/Wear-Caps-Chunsam-3.png",
    "https://i.ibb.co/V2JDTcR/Wear-Caps-Concon-1.png",
    "https://i.ibb.co/3RH3P5S/Wear-Caps-Concon-2.png",
    "https://i.ibb.co/hMvCBVY/Wear-Caps-Concon-3.png",
    "https://i.ibb.co/bQLD7Nh/Wear-Caps-Duckee-0.png",
    "https://i.ibb.co/P9cCHRD/Wear-Caps-Duckee-1.png",
    "https://i.ibb.co/ZYZ1wSq/Wear-Caps-Duckee-2.png",
    "https://i.ibb.co/SrwCV4R/Wear-Caps-Duckee-3.png",
    "https://i.ibb.co/9vyRjhr/Wear-Caps-Peach-0.png",
    "https://i.ibb.co/mS3Xq66/Wear-Caps-Peach-1.png",
    "https://i.ibb.co/PFnqhy7/Wear-Caps-Peach-2.png",
    "https://i.ibb.co/xDtmHFW/Wear-Caps-Peach-3.png",
    "https://i.ibb.co/fSFHMg7/Wear-Caps-Peepee-0.png",
    "https://i.ibb.co/swxfTDH/Wear-Caps-Peepee-1.png",
    "https://i.ibb.co/R4FTjgy/Wear-Caps-Peepee-2.png",
    "https://i.ibb.co/4jrNfGr/Wear-Caps-Peepee-3.png",
    "https://i.ibb.co/5sYRMJK/Wear-Hoodie-Chunsam-0.png",
    "https://i.ibb.co/0nk89PV/Wear-Hoodie-Chunsam-1.png",
    "https://i.ibb.co/68NpV0r/Wear-Hoodie-Chunsam-2.png",
    "https://i.ibb.co/MNzPVVZ/Wear-Hoodie-Chunsam-3.png",
    "https://i.ibb.co/1rxsxP8/Wear-Hoodie-Concon-1.png",
    "https://i.ibb.co/LkZfC8M/Wear-Hoodie-Concon-2.png",
    "https://i.ibb.co/jJQT1Tz/Wear-Hoodie-Concon-3.png",
    "https://i.ibb.co/hd5PXk5/Wear-Hoodie-Concon-4.png",
    "https://i.ibb.co/1MR5WQt/Wear-Hoodie-Duckee-0.png",
    "https://i.ibb.co/TLPqPs5/Wear-Hoodie-Duckee-1.png",
    "https://i.ibb.co/G3BXKWk/Wear-Hoodie-Duckee-2.png",
    "https://i.ibb.co/85P4pY3/Wear-Hoodie-Duckee-3.png",
    "https://i.ibb.co/6ntH6vX/Wear-Hoodie-Duckee-4.png",
    "https://i.ibb.co/tpmDV8x/Wear-Hoodie-Duckee-5.png",
    "https://i.ibb.co/60sYGC3/Wear-Hoodie-Duckee-6.png",
    "https://i.ibb.co/HY3v8F0/Wear-Hoodie-Duckee-7.png",
    "https://i.ibb.co/zQ59KJR/Wear-Hoodie-Peach-0.png",
    "https://i.ibb.co/LQ97b18/Wear-Hoodie-Peach-1.png",
    "https://i.ibb.co/MgQgKnk/Wear-Hoodie-Peach-2.png",
    "https://i.ibb.co/MgQgKnk/Wear-Hoodie-Peach-2.png",
    "https://i.ibb.co/jznxfxJ/Wear-Hoodie-Peepee-0.png",
    "https://i.ibb.co/1ngt2nk/Wear-Hoodie-Peepee-1.png",
    "https://i.ibb.co/d2hnr57/Wear-Hoodie-Peepee-2.png",
    "https://i.ibb.co/v1rmJHS/Wear-Hoodie-Peepee-3.png",
    "https://i.ibb.co/YB1Qzzg/Wear-Shirts-Chunsam-0.png",
    "https://i.ibb.co/W2DfQHg/Wear-Shirts-Chunsam-1.png",
    "https://i.ibb.co/r74r4Zb/Wear-Shirts-Chunsam-2.png",
    "https://i.ibb.co/zsMk9Mf/Wear-Shirts-Chunsam-3.png",
    "https://i.ibb.co/wpbRF18/Wear-Shirts-Chunsam-4.png",
    "https://i.ibb.co/rt8dsPH/Wear-Shirts-Chunsam-5.png",
    "https://i.ibb.co/hCbskwQ/Wear-Shirts-Concon-0.png",
    "https://i.ibb.co/SBYmm8d/Wear-Shirts-Concon-2.png",
    "https://i.ibb.co/5sWvM8R/Wear-Shirts-Concon-3.png",
    "https://i.ibb.co/kDYqtfz/Wear-Shirts-Concon-4.png",
    "https://i.ibb.co/q0rxfww/Wear-Shirts-Concon-5.png",
    "https://i.ibb.co/kDYqtfz/Wear-Shirts-Concon-4.png",
    "https://i.ibb.co/dpzb5RR/Wear-Shirts-Concon-7.png",
    "https://i.ibb.co/FDXrBFm/Wear-Shirts-Duckee-0.png",
    "https://i.ibb.co/ZMyVHGr/Wear-Shirts-Duckee-1.png",
    "https://i.ibb.co/pb033Xj/Wear-Shirts-Duckee-2.png",
    "https://i.ibb.co/3f5qNVq/Wear-Shirts-Duckee-3.png",
    "https://i.ibb.co/6s7Wf8W/Wear-Shirts-Duckee-4.png",
    "https://i.ibb.co/J2xzwqg/Wear-Shirts-Peach-0.png",
    "https://i.ibb.co/QpR0Wct/Wear-Shirts-Peach-1.png",
    "https://i.ibb.co/31wm3cn/Wear-Shirts-Peach-2.png",
    "https://i.ibb.co/nLLJgzz/Wear-Shirts-Peach-3.png",
    "https://i.ibb.co/6rTqZYq/Wear-Shirts-Peach-4.png",
    "https://i.ibb.co/zZkFgDG/Wear-Shirts-Peepee-0.png",
    "https://i.ibb.co/n3cVNFq/Wear-Shirts-Peepee-1.png",
    "https://i.ibb.co/YjW7cd3/Wear-Shirts-Peepee-2.png",
    "https://i.ibb.co/X4chPct/Wear-Shirts-Peepee-3.png",
    "https://i.ibb.co/rGKryjN/Wear-Shirts-Peepee-4.png",
    "https://i.ibb.co/MRJhRfq/Wear-Shirts-Peepee-5.png",
]

DETAIL_CONTENTS = {
    'Electronics': 
'''
<ul class="descriptionList">
  <li>
    <h2>콘콘 스마트폰</h2>
    <p class="productDescription">
      5G 스피드. 스마트폰 사상 가장 빠른 A14 Bionic 칩. 전면 화면 OLED 디스플레이.<br /> 
      4배 나은 낙하 성능을 선사하는 Ceramic Shield.<br /> 
      그리고 모든 카메라에서 지원되는 ‘야간 모드’까지.<br /> 
      이 모든 것을 담은 콘콘 스마트폰, 두 가지 완벽한 사이즈로 만날 수 있습니다.<br />
    </p>
  </li>
  <li>
    <img
      class="desImg"
      alt="상세이미지 1"
      src="https://i.ibb.co/n7cYbbC/Electronics-Phone-Peepee-4.png"
      id="1"
    />
  </li>
  <li>
    <img
      class="desImg"
      alt="상세이미지 2"
      src="https://i.ibb.co/pbPjH20/Electronics-Phone-Chunsam-0.png"
      id="2"
    />
  </li>
  <li>
    <img
      class="desImg"
      alt="상세이미지 3"
      src="https://i.ibb.co/HDm5Wd7/Electronics-Watch-Duckee-2.png"
      id="3"
    />
  </li>
  <li>
    <img
      class="desImg"
      alt="상세이미지 4"
      src="https://i.ibb.co/p2D4zdc/Electronics-Watch-Concon-2.png"
      id="4"
    />
  </li>
  <li>
    <img
      class="desImg"
      alt="상세이미지 5"
      src="https://i.ibb.co/PDfLdWt/Electronics-Imac-Peepee-8.png"
      id="5"
    />
  </li>
  <li>
    <img
      class="desImg"
      alt="상세이미지 6"
      src="https://i.ibb.co/fnhppMJ/Electronics-Imac-Concon-0.png"
      id="6"
    />
  </li>
  <li>
    <img
      class="desImg"
      alt="상세이미지 7"
      src="https://i.ibb.co/86S6tZv/group-Image.jpg"
      id="7"
    />
  </li>
  <li>
    <h2>콘콘 스마트폰</h2>
    <p class="productDescription">
      초고속 스피드를 자랑하는 iPhone의 5G.<br /> 
      영화 몇 편을 순식간에 다운로드하고, 고화질 동영상을 가뿐하게 스트리밍하고, 훨씬 적은 지연 시간으로 멀티플레이어 게임을 즐길 수 있게 해줍니다.<br /> 
      통신 환경이나 상황에 따라 5G와 LTE를 자동으로 오가는 스마트 데이터 모드 덕분에 배터리를 절약할 수 있는 것은 물론, 기기 자체에서 5G와 LTE 대역도 그 어느 때보다 다양하게 지원하기 때문에 그 모든 것을 세계 더 많은 곳에서 누릴 수 있죠.
    </p>
  </li>
</ul>
''',
    'Living':
'''
<ul class="descriptionList">
  <li>
    <h2>콘콘 플래너</h2>
    <p class="productDescription">
      계획을 쓰는 것 만으로도 실행율이 3배 이상 높아집니다.<br />
      생각만 하고 있었던 계획들, 일단 써보세요.
      콘콘 플래너와 함께 시작하세요.
    </p>
  </li>
  <li>
    <img
      class="desImg"
      alt="상세이미지 1"
      src="https://i.ibb.co/KDSfn38/Living-Books-Chunsam-1.png"
      id="1"
    />
  </li>
  <li>
    <img
      class="desImg"
      alt="상세이미지 2"
      src="https://i.ibb.co/KGn42Jn/Living-Books-Concon-2.png"
      id="2"
    />
  </li>
  <li>
    <img
      class="desImg"
      alt="상세이미지 3"
      src="https://i.ibb.co/bNfC4xM/001.png"
      id="3"
    />
  </li>
  <li>
    <img
      class="desImg"
      alt="상세이미지 4"
      src="https://i.ibb.co/W6jnkjW/Living-Books-Peach-3.png"
      id="4"
    />
  </li>
  <li>
    <img
      class="desImg"
      alt="상세이미지 5"
      src="https://i.ibb.co/tD02SvN/Living-Cup-Duckee-1.png"
      id="5"
    />
  </li>
  <li>
    <img
      class="desImg"
      alt="상세이미지 6"
      src="https://i.ibb.co/BCnv7tX/Living-Cup-Duckee-2.png"
      id="6"
    />
  </li>
  <li>
    <img
      class="desImg"
      alt="상세이미지 7"
      src="https://i.ibb.co/4gsyXbQ/Living-Cup-Duckee-3.png"
      id="7"
    />
  </li>
  <li>
    <img
      class="desImg"
      alt="상세이미지 8"
      src="https://i.ibb.co/XFkWXNs/group-Image.jpg"
      id="8"
    />
  </li>
  <li>
    <h2>콘콘 플래너</h2>
    <p class="productDescription">
      계획을 세우고 성취를 반복하는 것은 <br />
      강력한 동기부여가 됩니다. <br />
      콘콘 플래너가 당신을 내일로 나아가게 하는 원동력이 될거에요.
    </p>
  </li>
</ul>
''',
    'Wear':
'''
<ul class="descriptionList">
  <li>
    <h2>콘콘 비니비니</h2>
    <p class="productDescription">
      포근하게 머리를 감싸주는 콘콘 숏 비니를 만나보세요. <br />
      콘콘 비니는 머리에 꼭 맞는 둥근 모자입니다. <br />
      항균 기능이 있어 쾌적하며, 표면이 깨끗하고 고른 외관의 소재로 만들었습니다. <br />
      가볍고 부드러운 착용감을 제공합니다.
    </p>
  </li>
  <li>
    <img
      class="desImg"
      alt="상세이미지 1"
      src="https://i.ibb.co/hMvCBVY/Wear-Caps-Concon-3.png"
      id="1"
    />
  </li>
  <li>
    <img
      class="desImg"
      alt="상세이미지 2"
      src="https://i.ibb.co/mS3Xq66/Wear-Caps-Peach-1.png"
      id="2"
    />
  </li>
  <li>
    <img
      class="desImg"
      alt="상세이미지 3"
      src="https://i.ibb.co/mc0mjc8/Wear-Caps-Chunsam-3.png"
      id="3"
    />
  </li>
  <li>
    <img
      class="desImg"
      alt="상세이미지 4"
      src="https://i.ibb.co/SrwCV4R/Wear-Caps-Duckee-3.png"
      id="4"
    />
  </li>
  <li>
    <img
      class="desImg"
      alt="상세이미지 5"
      src="https://i.ibb.co/bJKTL28/Wear-Caps-Chunsam-0.png"
      id="5"
    />
  </li>
  <li>
    <img
      class="desImg"
      alt="상세이미지 6"
      src="https://i.ibb.co/PFnqhy7/Wear-Caps-Peach-2.png"
      id="6"
    />
  </li>
  <li>
    <img
      class="desImg"
      alt="상세이미지 7"
      src="https://i.ibb.co/ZYZ1wSq/Wear-Caps-Duckee-2.png"
      id="7"
    />
  </li>
  <li>
    <img
      class="desImg"
      alt="상세이미지 8"
      src="https://i.ibb.co/k22qjwb/group-Image.jpg"
      id="8"
    />
  </li>
  <li>
    <h2>콘콘 비니비니</h2>
    <p class="productDescription">
      포근하게 머리를 감싸주는 콘콘 숏 비니를 만나보세요. <br />
      콘콘 비니는 머리에 꼭 맞는 둥근 모자입니다. <br />
      항균 기능이 있어 쾌적하며, 표면이 깨끗하고 고른 외관의 소재로 만들었습니다. <br />
      가볍고 부드러운 착용감을 제공합니다.
    </p>
  </li>
</ul>
''',
}