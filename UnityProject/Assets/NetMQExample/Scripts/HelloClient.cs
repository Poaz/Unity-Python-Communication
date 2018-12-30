using UnityEngine;

public class HelloClient : MonoBehaviour
{
    private HelloRequester _helloRequester;
    public bool StopCom;

    void Update()
    {
        if (StopCom == true)
        {
            _helloRequester.Stop();
        } else
        {
        }

    }

    private void Start()
    {
        _helloRequester = new HelloRequester();
        _helloRequester.Start();
    }

    private void OnDestroy()
    {
        _helloRequester.Stop();
    }
}