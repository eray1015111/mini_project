var qoutearray=[
{
	"author":"虎杖悠仁(いたどりゆうじ)",
	"quote":"自分が死ぬ時のことは分からんけど 生き様で後悔はしたくない"
},
{
	"author":"伏黒恵(ふしぐろめぐみ)",
	"quote":"俺は不平等に人を助ける"},
{
	"author":"釘崎野薔薇(くぎさきのばら)",
	"quote":"懸けられるわ 私が私であるためだもの"},
{
	"author":"五条悟(ごじょうさとる)",
	"quote":"周りに味方が何人いようと 死ぬときは独りだよ"},
{
	"author":"七海建人(ななみけんと)",
	"quote":"後は頼みます"},
{
	"author":"真人(まひと)",
	"quote":"みんな言葉遊びが好きなのさ。なぜなら人間は、言い訳をしないと生きていけないからね"},
{
	"author":"伏黒津美紀(ふしぐろつみき)",
	"quote":"誰かを呪う暇があったら 大切な人のことを考えていたいの"},
	{
	"author":"虎杖倭助(いたどりわすけ)",
	"quote":"悠仁。お前は強いから人を助けろ。手の届く範囲でいい、救える奴は救っとけ。迷ってもいい、感謝されなくても気にするな。とにかく1人でも多く助けてやれ"},
	{
	"author":"虎杖悠仁(いたどりゆうじ)",
	"quote":"正しい死に様なんて分かりゃしない　ならせめて分かるまでアイツを殺すまで　もう俺は負けない"}

]
function randomselect(arrayLength){
	return Math.floor(Math.random()*arrayLength);
}
function generateQuote(){
	var randomnum=randomselect(qoutearray.length);
	document.getElementById("quoteOutput").innerHTML='"'+qoutearray[randomnum].quote+'"'
	document.getElementById("authorOutput").innerHTML='"'+qoutearray[randomnum].author+'"'
}