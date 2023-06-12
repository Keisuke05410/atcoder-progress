# atcoder-progress
## アプリ概要
**atcoder-progress**とはatcoderで解いた問題を管理するアプリです。
![image](https://github.com/Keisuke05410/atcoder-progress/assets/113495285/67834281-00ed-4204-9089-10ac1b99085d)

## 使用技術
### フロントエンド
- HTML
- CSS
- Bootstrap
### バックエンド
- python
- Flask
- Flask-sql-alchemy
### インフラ
- Heroku

## 機能一覧
- 問題の追加  
一番上の入力欄に問題の載っているURLをペーストし、問題を追加することができる。  
また、自動で大会、番号、問題番号を自動で識別し区別している。
![image](https://github.com/Keisuke05410/atcoder-progress/assets/113495285/7d87b472-8d6f-49b6-8413-30dd4f378634)

- 追加した問題の修正  
右側の赤と青のボタンから編集、削除をすることができる。
![image](https://github.com/Keisuke05410/atcoder-progress/assets/113495285/122019b2-20e5-423f-b10e-e1924c01802f)

- 間違えた問題の復習  
間違えた問題に対しては緑色の復習ボタンが表示される。
![image](https://github.com/Keisuke05410/atcoder-progress/assets/113495285/b69ae7f3-a53f-4da4-8223-d63e08494e1f)
そして解きなおして正解した場合には、それがわかるように表示し、復習しやすいようにする。
![image](https://github.com/Keisuke05410/atcoder-progress/assets/113495285/159ad520-b32c-48df-bd7d-3294651f80e7)

## 今後実装したいもの
- 問題へのタグ付け
- ChatGPTのAPIと連携してコードの解説を行う機能
- より洗練されたUI
- Chrome拡張機能を用いた問題の追加
