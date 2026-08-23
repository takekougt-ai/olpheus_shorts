# プライバシーポリシー

本アプリ(olpheus_shorts)は、開発者本人が所有する Google アカウントの動画を
Google Drive から取得し、YouTube Shorts へ自動投稿するための個人利用ツールです。

## 取得する情報とスコープ

- `https://www.googleapis.com/auth/drive.readonly`
  Google Drive 内の指定フォルダにある動画ファイルの一覧取得・ダウンロードのみに使用します。
- `https://www.googleapis.com/auth/youtube.upload`
  取得した動画を YouTube チャンネルにアップロードするためだけに使用します。

## データの利用・共有

- 取得したデータは、動画のダウンロードとアップロードの処理にのみ使用し、
  開発者本人が管理する GitHub Actions の実行環境以外には送信しません。
- 取得したデータを第三者と共有、販売、broadcastすることはありません。
- アプリは開発者本人のみが使用し、他のユーザーへの提供は行っていません。

## お問い合わせ

本アプリに関するお問い合わせは、リポジトリの Issue または以下の連絡先までお願いします。

- Email: takekougt@gmail.com
